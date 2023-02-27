from flask import Flask
from os import getenv 
import requests

app = Flask(__name__)

@app.route("/")
def hello_world():
        return "<p>Hello world</p>"




@app.route("/books")
def get_books():
        payload = {"list":"hardcover-fiction", "api-key": getenv("NYT_API_KEY") }
        print(getenv("NYT_API_KEY")) 
        r = requests.get("https://api.nytimes.com/svc/books/v3/lists.json", params=payload)
        print(r.url)
        return r.text


