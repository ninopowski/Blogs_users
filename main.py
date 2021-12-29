from flask import Flask, render_template, url_for, request
from forms import Post
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config["SECRET_KEY"] = "verysecretkey"
Bootstrap(app)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/new-post", methods=["GET", "POST"])
def new_post():
    form = Post()
    return render_template("new_post.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)