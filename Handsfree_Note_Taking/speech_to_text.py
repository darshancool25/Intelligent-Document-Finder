import speech_recognition as sr
import os
import sys

def record_until_interrupt():
    r = sr.Recognizer()
    chunks = []
    try:
        while(True):
            with sr.Microphone() as source:
                audio_data = r.record(source, duration = 5)
                chunks.append(audio_data)
    except KeyboardInterrupt:
        pass
    recorded_text = ""
    for chunk in chunks :
        recorded_text += r.recognize_google(chunk) + ' '
    return recorded_text