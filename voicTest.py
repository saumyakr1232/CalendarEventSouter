from gtts import gTTS
import playsound


eng = "ए चचा ए, शिल्पा के dekhah, जब हम आते ह तब ये आती है"
obj = gTTS(text=eng, slow=False, lang='hi')
obj.save('eng.mp3')


# engine.setProperty('rate', 120)
# engine.say(eng)
# engine.runAndWait()

# engine = pyttsx3.init()

while( True):
    playsound.playsound("eng.mp3")
