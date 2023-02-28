from flask import Flask, request, abort
from flask_cors import CORS
from os import getenv 
import requests

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route("/")
def hello_world():
        return "<p>Hello world</p>"


@app.route("/api/books")
def get_books():
        if request.args.get("token") == getenv("API_SECRET"):
                payload = {"list":"hardcover-fiction", "api-key": getenv("NYT_API_KEY") }
                r = requests.get("https://api.nytimes.com/svc/books/v3/lists.json", params=payload)
                return r.text
        else:
                abort(401)


