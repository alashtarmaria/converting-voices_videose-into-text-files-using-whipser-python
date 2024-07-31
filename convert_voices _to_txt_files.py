import ssl
import whisper
import os

# Disable SSL verification temporarily
ssl._create_default_https_context = ssl._create_unverified_context

# load the whisper model
model = whisper.load_model("medium")

print("Model loaded successfully")

# Path to the audio file
audio_path = "/Users/Downloads/test.mp3"

# Check if the audio file exists
if not os.path.isfile(audio_path):
    raise FileNotFoundError(f"Audio file not found at path: {audio_path}")

# Transcribe the audio file
result = model.transcribe(audio_path)

# Path to save the transcription
output_path = "/Users/Downloads/Test/dene.txt"

# Write the transcription to a text file
with open(output_path, "w") as file:
    file.write(result["text"])

print("Transcription done successfully")

