from flask import Flask, request, jsonify, render_template
import whisper
import sounddevice as sd
from scipy.io.wavfile import write
import os
from werkzeug.utils import secure_filename

# Initialize Flask app and Whisper model
app = Flask(__name__)
model = whisper.load_model("base")

# Allowed file extensions
ALLOWED_EXTENSIONS = {'mp3', 'wav', 'm4a', 'aac', 'ogg'}

# Directory to save uploaded files
UPLOAD_FOLDER = './uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Check if file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle file uploads
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Transcribe the audio file
        result = model.transcribe(filepath)
        return jsonify({'transcription': result['text']}), 200
    return jsonify({'error': 'Invalid file type'}), 400

# Route to handle audio recording
@app.route('/record', methods=['POST'])
def record_audio():
    duration = int(request.form.get('duration', 5))  # Default duration: 5 seconds
    sample_rate = 44100  # Sampling rate
    try:
        recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2)
        sd.wait()  # Wait for recording to finish
        recording_file = os.path.join(app.config['UPLOAD_FOLDER'], 'recorded_audio.wav')
        write(recording_file, sample_rate, recording)

        # Transcribe the recorded audio
        result = model.transcribe(recording_file)
        return jsonify({'transcription': result['text']}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
