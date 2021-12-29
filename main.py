from flask import Flask, render_template, url_for, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/new-post")
def new_post():
    return render_template("new_post.html")


if __name__ == "__main__":
    app.run(debug=True)