from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World! This is from Python Flask Home Page"

@app.route('/about')
def about():
    return "<h2> Hello World from About page </h2>"

@app.route('/profile/<name>')
def profile(name):
    return render_template("Profile.html",name=name)
