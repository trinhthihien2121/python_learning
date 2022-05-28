from flask import Flask, render_template
 
app = Flask (__name__)

@app.route("/")
def index():
    return "Hello,world!"

@app.route("/Hiencute")
def index1():
    return"Hello,hiencute!"

@app.route("/linh")
def index2():
    return"hello,linh!"

@app.route('/my')
def my():
    return render_template('fist1.html')

