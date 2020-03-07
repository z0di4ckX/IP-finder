from flask import Flask, redirect, url_for
import ip_finder

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! this is the main page <h1>Hello</h1>"

@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

# Working on it!
@app.route("/ip_finder")
def ip():
    return(ip_finder)

@app.route("/admin")
def admin():
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run()