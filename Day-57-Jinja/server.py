import random
from datetime import datetime
from flask import Flask , render_template
import requests
URL = "https://api.agify.io"
app = Flask(__name__)

@app.route('/')
def home():
    current_year = datetime.now().year
    random_number = random.randint(1,10)
    return render_template("index.html", num = random_number, year = current_year)

@app.route('/guess/<name>')
def age(name):
    response = requests.get(f"https://api.agify.io?name={name}")
    data = response.json()
    name = data["name"]
    old = data["age"]
    return render_template("index.html", name = name, old = old)

@app.route('/blog/<number>')
def get_blog(number):
    print(number)
    blog_url = "https://api.npoint.io/ecfe5890e4857ae9911f"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html",posts= all_posts)

if __name__ == "__main__":
    app.run(debug=True)