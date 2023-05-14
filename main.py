from flask import Flask, render_template, request
import replicate
import os
from PIL import Image
from urllib.request import urlretrieve
import io
import base64

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            input_image = file.read()

            os.environ["REPLICATE_API_TOKEN"] = "r8_LZfmm9k12VophK1NfiV287xk8u5amry2atIYp"


            output = replicate.run(
                "nightmareai/real-esrgan:42fed1c4974146d4d2414e2be2c5277c7fcf05fcc3a73abf41610695738c1d7b",
                input={"image": io.BytesIO(input_image)}
            )

            # Download the image
            urlretrieve(output, "out.jpg")

            # Open the downloaded image
            image = Image.open("out.jpg")

            # Convert the image to base64 so it can be displayed in HTML
            buffered = io.BytesIO()
            image.save(buffered, format="JPEG")
            img_str = base64.b64encode(buffered.getvalue()).decode()

            return render_template('display.html', img_data=img_str)

    return render_template('upload.html')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
