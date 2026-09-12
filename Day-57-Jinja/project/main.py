from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def home():
    blog_url = "https://api.npoint.io/ecfe5890e4857ae9911f"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)

@app.route('/post/<int:id>')
def get_post(id):
    blog_url = "https://api.npoint.io/ecfe5890e4857ae9911f"
    response = requests.get(blog_url)
    all_posts = response.json()

    requested_post = None

    for post in all_posts:
        if post["id"] == id:
            requested_post = post
            break

    return render_template("post.html", post=requested_post)
if __name__ == "__main__":
    app.run(debug=True)
