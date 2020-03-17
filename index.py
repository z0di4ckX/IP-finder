from flask import Flask, redirect, url_for, render_template
#import ip_finder
app = Flask(__name__)

@app.route("/<name>")
def home(name):
    return render_template("index.html", content=name)

# @app.route("/<name>")
# def user(name):
#     return f"Hello {name}!"

# # Working on it!
# @app.route("/<ipF>")
# def ip(ipF):
#     return f"{ipF}"

# @app.route("/admin")
# def admin():
#     return redirect(url_for("user", name="Admin!"))

if __name__ == "__main__":
    app.run()