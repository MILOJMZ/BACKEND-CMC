from flask import Flask, render_template, request 
import cloudinary
import cloudinary.uploader

app = Flask(__name__)

cloudinary.config(
    cloud_name = 'dpclur0cs',
    api_key = '234837349421278',
    api_secret = '6STT8rCM4iHmqjO5Cwf8ZbN8mFU'
)

@app.route('/certificados', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        image_url = "files"
        return render_template('certificado.html', image_url=image_url)
    else:
        return render_template('certificado.html')
        
if __name__ == '__main__':
    app.run(debug=True)