from flask import Flask, render_template
import json

db_file = open("db.json", "r")
blog_data = json.load(db_file)["data"]

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/configurator")
def configurator():
    return render_template("configurator.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/blog")
def blog():
    return render_template("blog.html", data=blog_data)

@app.route("/blog/<int:id>")
def blog_post(id):
    for post in blog_data:
        if post["id"] == id:
            print(id)
            title=post["title"]
            content=post["content"]
            img=post["img"]
            return render_template("blog_post.html", title=title, content=content, img=img)
    return render_template("blog.html", data=blog_data)