from flask import Flask, render_template, url_for, request, redirect
from forms import Post
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = "verysecretkey"

Bootstrap(app)

#db setup
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Blogs.db"
db = SQLAlchemy(app)

class BlogPost(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    author = db.Column(db.String(150), nullable=False)
    body = db.Column(db.String, nullable=False)

#run only once
db.create_all()




@app.route("/")
def home():
    posts = BlogPost.query.all()
    return render_template("index.html", posts=posts)


@app.route("/new-post", methods=["GET", "POST"])
def new_post():
    form = Post()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            author=form.author.data,
            body=form.body.data
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("new_post.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)