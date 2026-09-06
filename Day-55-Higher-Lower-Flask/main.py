from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    # This will be shown im your browser
    return 'Hello, World!'

@app.route('/bye')
def say_bye():
    return "Byeee!!!!"

@app.route('/username/<name>')
def greet_user(name):
    return f"Hello {name}"

if __name__ == "__main__":
    app.run(debug=True)