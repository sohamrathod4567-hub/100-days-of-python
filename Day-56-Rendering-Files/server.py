# from flask import Flask , render_template
#
# app = Flask(__name__)
#
# @app.route("/")
# def home():
#     return render_template("index.html")
#
# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, render_template
import os

app = Flask(__name__)

print("Root path:", app.root_path)
print("Template folder:", app.template_folder)
print(
    "Index exists:",
    os.path.exists(os.path.join(app.root_path, "templates", "index.html"))
)


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)