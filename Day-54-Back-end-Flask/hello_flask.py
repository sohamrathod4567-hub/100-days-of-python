import time
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    # This will be shown im your browser
    return 'Hello, World!'

@app.route('/bye')
def say_bye():
    return "Byeee!!!!"

if __name__ == "__main__":
    app.run()


# def delay_decorator(function):
#     def wrapper_function():
#         time.sleep(2)
#         #DO Something Before
#         function()
#         #Do Something After
#     return wrapper_function
#
# @delay_decorator
# def say_hello():
#     print("Hello World")
#
# def say_ola():
#     print("Ola Amigos")
#
# say_hello()
# say_ola()
