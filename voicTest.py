from gtts import gTTS
import playsound
import pyttsx3

# TODO


eng = "सर nishant c  है हम क्या करें  "
obj = gTTS(text=eng, slow=False, lang='hi')
obj.save('eng.mp3')


# engine.setProperty('rate', 120)
# engine.say(eng)
# engine.runAndWait()

# engine = pyttsx3.init()

while( True):
    playsound.playsound("eng.mp3")
