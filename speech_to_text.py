# Do not name the file as speech_recogntion and avoid making functions with the name speech recognition, it might cause errors due to circular imports.
import speech_recognition as sr

def speech_to_text():
    r = sr.Recognizer()
    try :
        with sr.Microphone() as source:
            audio = r.listen(source)
            text = r.recognize_google(audio)
    except Exception:
        text = ''
    
    return text

