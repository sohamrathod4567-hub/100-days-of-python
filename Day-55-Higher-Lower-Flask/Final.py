from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return (
        "<h1>Guess the Number between 0 and 9</h1>"
        '<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcWh2cDJxMjlyZzFpNjkycHJnbGZ1cHo5ZTJhano4ZWNrMXd6b21kYyZlcD12MV9naWZzX3RyZW5kaW5nJmN0PWc/ASd0Ukj0y3qMM/giphy.gif">'
    )


if __name__ == "__main__":
    app.run(debug=True)