from flask import Flask, render_template
import requests

posts = requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()
app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


@app.route("/post")
def show_post():
    return render_template("post.html")

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == '__main__':
    app.run(debug=True)
