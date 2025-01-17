import sounddevice as sd
import numpy as np
import wavio
import speech_recognition as sr


def record_and_translate_to_text():
    duration = 10
    fs = 44100 

    print("Recording started")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=2, dtype='int16')
    sd.wait()
    print("Recording completed")
    wavio.write("recording.wav", recording, fs, sampwidth=2)
    recognizer = sr.Recognizer()

    with sr.AudioFile('recording.wav') as source:
        audio = recognizer.record(source)

    try:
      text = recognizer.recognize_google(audio)
    except sr.UnknownValueError as uve:
       print(f"Error: {uve}")
    except sr.RequestError as e:
      print(f"Unable to access Google API: {e}")
    return text
