from flask import render_template, url_for, flash, redirect, request
from app import app
from app.forms import RegistrationForm, LoginForm, BlogForm
from app.models import User, Blog, Entry
from flask_login import login_user, current_user, logout_user, login_required
import sqlite3

def get_db_connection():
    conn = sqlite3.connect('site.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
@app.route("/home")
def home():
    conn = get_db_connection()
    blogs = conn.execute('SELECT * FROM blogs').fetchall()
    conn.close()
    return render_template('home.html', blogs=blogs)

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        conn = get_db_connection()
        conn.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)',
                     (form.username.data, form.email.data, form.password.data))
        conn.commit()
        conn.close()
        flash('Your account has been created!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE email = ?', (form.email.data,)).fetchone()
        conn.close()
        if user and user['password'] == form.password.data:
            login_user(User(user['id']), remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/blog/new", methods=['GET', 'POST'])
@login_required
def new_blog():
    form = BlogForm()
    if form.validate_on_submit():
        conn = get_db_connection()
        conn.execute('INSERT INTO blogs (title, user_id) VALUES (?, ?)',
                     (form.title.data, current_user.id))
        conn.commit()
        conn.close()
        flash('Your blog has been created!', 'success')
        return redirect(url_for('home'))
    return render_template('create_blog.html', title='New Blog', form=form, legend='New Blog')

@app.route("/blog/<int:blog_id>")
def blog(blog_id):
    conn = get_db_connection()
    blog = conn.execute('SELECT * FROM blogs WHERE id = ?', (blog_id,)).fetchone()
    conn.close()
    return render_template('blog.html', title=blog['title'], blog=blog)
