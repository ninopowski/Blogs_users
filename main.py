from flask import Flask, render_template, url_for, request, redirect
from forms import PostForm, RegisterForm
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

#flask setup
app = Flask(__name__)
app.config["SECRET_KEY"] = "verysecretkey"

Bootstrap(app)

#db setup
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Blogs.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

#login menager setup
login_menager = LoginManager()
login_menager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class BlogPost(db.Model):
    __tablename__ = "blog_post"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    author = db.Column(db.String(150), nullable=False)
    body = db.Column(db.String, nullable=False)

#run only oncw
#db.create_all()

class User(db.Model):
    __tablename__ = "Users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String, nullable=False)

db.create_all()


@app.route("/")
def home():
    posts = BlogPost.query.all()
    return render_template("index.html", posts=posts)


@app.route("/register")
def register():
    form = RegisterForm()
    pass

@app.route("/new-post", methods=["GET", "POST"])
def new_post():
    form = PostForm()
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