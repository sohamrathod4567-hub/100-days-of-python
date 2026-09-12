from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def home():
    blog_url = "https://api.npoint.io/ecfe5890e4857ae9911f"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)

@app.route('/post/<id>')
def get_post(id):
    post_id = id
    return render_template("post.html", post_id=post_id)

if __name__ == "__main__":
    app.run(debug=True)
