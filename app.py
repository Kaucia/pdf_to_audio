
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
import pdfplumber
from gtts import gTTS

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'pdf'}

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def pdf_to_text(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def text_to_audio(text, filename):
    tts = gTTS(text=text, lang='en')
    tts.save(filename)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        text = pdf_to_text(file_path)
        audio_filename = filename.rsplit('.', 1)[0] + '.mp3'
        audio_path = os.path.join(app.config['UPLOAD_FOLDER'], audio_filename)
        text_to_audio(text, audio_path)
        return render_template('index.html', audio_file=audio_filename)
    return redirect(request.url)


if __name__ == '__main__':
    app.run(debug=True)
