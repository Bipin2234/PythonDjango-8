
import speech_recognition as sr
import webbrowser as wb

r1 = sr.Recognizer()

with sr.Microphone as source:
    print("speak")
    audio = r1.listen(source)
text=r1.recognize_google(audio)
print(text)
