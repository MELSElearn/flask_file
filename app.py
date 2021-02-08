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
    imagefile = flask.request.files.get('imagefile', '')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
    imagefile = flask.request.files.get('imageUpload', '')
    #f = request.files['file']
    #f.save(secure_filename(f.filename))
    #return 'file uploaded successfully'
      
    


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
