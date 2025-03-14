from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id, username=None, email=None, password=None):
        self.id = id
        self.username = username
        self.email = email
        self.password = password

class Blog:
    def __init__(self, id, title, user_id):
        self.id = id
        self.title = title
        self.user_id = user_id

class Entry:
    def __init__(self, id, title, content, blog_id):
        self.id = id
        self.title = title
        self.content = content
        self.blog_id = blog_id
