from flask import Flask
mongo_snippets = Flask(__name__)

@mongo_snippets.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    mongo_snippets.run()