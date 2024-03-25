from vosk import Model , KaldiRecognizer

import pyaudio

model = Model(r"C:\Users\poppo\Desktop\github ai\end to end by vivek\repo-53-speech-to-text-models\vosk\vosk-model-small-hi-0.22")


recognizer = KaldiRecognizer(model , 16000)

mic = pyaudio.PyAudio()
stream = mic.open(rate=16000,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=8192)
stream.start_stream()

while True:
    data = stream.read(4096)
    if recognizer.AcceptWaveform(data):
        print(recognizer.Result())