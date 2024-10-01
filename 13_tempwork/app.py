# Princeden, Tim 
# SegFault
# SoftDev
# K13 -- Combine
# 2024-09-30
# Time: N/A

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "No hablo queso!"

@app.route("/wdywtbwygp") 
def test_tmplt():
    return render_template('main.html', title = "Occupations")


if __name__ == "__main__":
    app.debug = True
    app.run()