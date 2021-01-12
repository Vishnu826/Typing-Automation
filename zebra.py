import pyautogui
import speech_recognition as sr
listener=sr.Recognizer()
with sr.Microphone as source:
    listener.adjust_for_ambient_noise(source, duration=0.2)
    sound=listener.listen(source)
    text=listener.recognize_google(sound)
    text=text.lower()
def enter():
    pyautogui.typewrite(text)
    pyautogui.press("enter")
enter()

