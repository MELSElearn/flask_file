import os

from flask import Flask
from flask import render_template, request
from currency_converter import CurrencyConverter

app = Flask(__name__)


@app.route("/")
def form():
    return render_template("index.html")


@app.route("/", methods=["POST"])
def my_form_post():
   return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
