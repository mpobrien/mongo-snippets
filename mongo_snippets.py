from flask import Flask
from flask import render_template

mongo_snippets = Flask(__name__)

@mongo_snippets.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    mongo_snippets.debug = True
    mongo_snippets.run()
