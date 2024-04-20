#for using google transcriber
#with latency


import os
import pyaudio
import vosk
import json
import time
from googletrans import Translator

# Set the path to the Vosk model
MODEL_PATH = r"C:\Users\poppo\Desktop\downloads firefox\vosk models\vosk-model-small-en-us-0.15"

# Initialize the Vosk model
vosk.SetLogLevel(-1)
model = vosk.Model(MODEL_PATH)
rec = vosk.KaldiRecognizer(model, 20000)

# Initialize Google Translator
translator = Translator()

# Function to recognize speech from audio
def recognize_audio(audio):
    start_time = time.time()  # Record start time

    rec.AcceptWaveform(audio)

    # Get the recognized text
    result = json.loads(rec.FinalResult())
    result_text = result["text"]

    # Translate the recognized text to English
    translated_text = translator.translate(result_text, dest='hi').text

    end_time = time.time()  # Record end time
    latency = end_time - start_time  # Calculating the  latency
    
    return translated_text, latency

# function to capture audio from microphone with a duration limit
def capture_audio(duration, rate=16000, chunk=1024):
    audio = pyaudio.PyAudio()
    stream = audio.open(format=pyaudio.paInt16, channels=1, rate=rate, input=True, frames_per_buffer=chunk)
    print("Listening...")

    frames = []
    for i in range(0, int(rate / chunk * duration)):
        data = stream.read(chunk)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    audio.terminate()

    return b"".join(frames)

# Main function to continuously capture and recognize live audio
def main():
    while True:
        duration = 20  # Duration in seconds
        audio_data = capture_audio(duration)

        # Recognize the captured audio
        text, latency = recognize_audio(audio_data)
        print(f"Recognized (Translated): {text} (Latency: {latency:.2f} seconds)")

if __name__ == "__main__":
    main()
