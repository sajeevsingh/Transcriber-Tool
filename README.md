# Transcriber Tool

### **Description**
A web-based audio transcription tool built with Flask and Whisper AI. This tool allows users to upload audio files or record their voice directly and provides a transcription using advanced AI models.

---

### **Features**
- **Upload Audio Files**: Supports `.mp3`, `.wav`, and other formats.
- **Record Audio**: Record directly from the browser and transcribe.
- **Real-Time Feedback**: Includes progress indicators and animations.
- **User-Friendly UI**: Interactive and visually appealing design.

---

### **Setup Instructions**

#### **Step 1: Clone the Repository**
```bash
git clone https://github.com/sajeevsingh/Transcriber-Tool
cd TranscriberTool
```
---

#### **Step 2: Create and Activate a Virtual Environment**
Create a virtual environment
```bash
python -m venv whisper_env
```
Activate the virtual environment
```bash
whisper_env\Scripts\activate
```
---

#### **Step 3: Install Dependencies**
Install required Python packages
```bash
pip install -r requirements.txt
```
---

#### **Step 4: Install FFmpeg**
Download FFmpeg
- Go to the official https://www.gyan.dev/ffmpeg/builds/
- Download the latest release essentials build.
Extract FFmpeg
- Extract the downloaded .zip file to a directory (e.g., C:\ffmpeg).
Add FFmpeg to Path
On Windows:

- Open the Start menu, search for Environment Variables, and click Edit the system environment variables.
- Under System Variables, find the Path variable and click Edit.
- Add the path to the bin folder inside the FFmpeg directory (e.g., C:\ffmpeg\bin).
- On macOS/Linux, install FFmpeg via your package manager:
```bash
brew install ffmpeg   # macOS with Homebrew
sudo apt install ffmpeg   # Ubuntu/Debian
```

Include FFmpeg in the Virtual Environment
- To make FFmpeg accessible in the virtual environment, add the following line to the activate script:

- On Windows: Edit whisper_env\Scripts\activate and add:
```bash
set PATH=%PATH%;C:\ffmpeg\bin
```

- On macOS/Linux: Edit whisper_env/bin/activate and add:
```bash
export PATH="$PATH:/usr/local/bin/ffmpeg"
```
---

#### **Step 5: Run the Application**

Start the Flask server
```bash
python app.py
```
Access the application
Open your browser and navigate to:
```bash
http://127.0.0.1:5000/
```

### **Latest Update**
- **Added Hindi Transcription Support**: Users can now transcribe Hindi audio files with improved accuracy. The latest update includes:
  - A dedicated Hindi transcription page.
  - Support for both file uploads and live audio recordings in Hindi.
  - Enhanced UI for switching between English, Hindi, and mixed-language transcription.

Check out the updated features and feel free to contribute!
