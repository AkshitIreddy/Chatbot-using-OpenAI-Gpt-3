import pyttsx3

# For gender, 0 is male and 1 is female.
def text_to_speech(text, gender = 0):	
  engine=pyttsx3.init('sapi5')
  voices=engine.getProperty('voices')
  engine.setProperty('voice', voices[gender].id)
  engine.say(text)
  engine.runAndWait()

