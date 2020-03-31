from gtts import gTTS
import playsound
import time
import datetime


eng = "ए चचा ए,   शिल्पा के dekhah, जब हम aaaye ni tabh uhoooo aawee laeee "

obj = gTTS(text=eng, slow=False, lang='hi')
obj.save('eng.mp3')


# engine.setProperty('rate', 120)
# engine.say(eng)
# engine.runAndWait()

# engine = pyttsx3.init()

while( True):
    playsound.playsound("eng.mp3")
    time.sleep(2)
