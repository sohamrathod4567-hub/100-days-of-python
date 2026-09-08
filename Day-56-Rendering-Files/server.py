from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/pablo")
def pablo():
    return render_template("pablo.html")

@app.route("/E1")
def e1():
    return render_template("E1.html")

if __name__ == "__main__":
    app.run(debug=True)

