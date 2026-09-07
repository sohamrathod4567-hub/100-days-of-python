from flask import Flask
app = Flask(__name__)

def bold_decorator(function):
    def wrapper_function():
        #DO Something Before
        result = function()
        return f"<b>{result}</b>"
        #Do Something After
    return wrapper_function






@app.route('/')
@bold_decorator
def hello_world():
    # This will be shown im your browser
    return 'Hello, World!'



if __name__ == "__main__":
    app.run(debug=True)

