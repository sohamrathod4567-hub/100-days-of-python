from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    # This will be shown im your browser
    return 'Hello, World!'