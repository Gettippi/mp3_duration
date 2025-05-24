from flask import Flask, request, jsonify
from mutagen.mp3 import MP3
import io

app = Flask(__name__)

@app.route('/mp3-duration', methods=['POST'])
def mp3_duration():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        audio = MP3(io.BytesIO(file.read()))
        duration = audio.info.length
        return jsonify({'duration_seconds': duration})
    except Exception as e:
        return jsonify({'error': str(e)}), 400
