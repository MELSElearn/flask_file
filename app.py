import os

from flask import Flask
from flask import render_template, request

from PIL import Image
import numpy as np
import cv2
from base64 import b64decode, b64encode

app = Flask(__name__)


@app.route("/")
def form():
    return render_template("index.html")


@app.route('/', methods = ['GET', 'POST'])
def upload_file():
  if request.method == 'POST':
    file = request.files['imageUpload'].read()

    nparr = np.frombuffer(file, dtype=np.uint8)

    print(nparr)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    Facecascde = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    faces = Facecascde.detectMultiScale(img_gray, 1.5, 3)
    for (x, y, w, h) in faces:
        print(x)
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    #f.save(secure_filename(f.filename))
    #return 'file uploaded successfully'
    #cv2_imshow(img)

    # turn image processed to base64
    
    #newimg = Image.fromarray(img.astype("uint8"))
    #rawBytes = io.BytesIO()
    #newimg.save(rawBytes, "JPEG")
    #rawBytes.seek(0)
    #img_base64 = base64.b64encode(rawBytes.read())

    _, im_arr = cv2.imencode('.png', img)  # im_arr: image in Numpy one-dim array format.
    im_bytes = im_arr.tobytes()
    im_b64 = b64encode(im_bytes)


    return render_template("index.html", user_image = im_b64)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
