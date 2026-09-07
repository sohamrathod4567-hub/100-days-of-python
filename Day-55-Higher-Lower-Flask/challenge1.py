from flask import Flask
app = Flask(__name__)

def bold_decorator(function):
    def wrapper_function():
        #DO Something Before
        result = function()
        return f"\033[1m{result}\033[0m"
        #Do Something After
    return wrapper_function






@app.route('/')
@bold_decorator
def hello_world():
    # This will be shown im your browser
    return 'Hello, World!'

