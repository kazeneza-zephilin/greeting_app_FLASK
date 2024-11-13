from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "JustRandomText"

@app.route("/hello")
def index():
    flash("what's your name please")
    return render_template("index.html")

@app.route("/greet", methods = ["POST", "GET"])
def greet():
    flash("Hi" + ' ' +  str(request.form['name_input']) +  ' ' + 'Welcome back!')
    return render_template("index.html")