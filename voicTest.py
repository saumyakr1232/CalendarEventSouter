from gtts import gTTS
import playsound
import pyttsx3


eng = "सर there is an emergency case of मेहर गिरेबान "
obj = gTTS(text=eng, slow=False, lang='hi')
obj.save('eng.mp3')


# engine.setProperty('rate', 120)
# engine.say(eng)
# engine.runAndWait()

# engine = pyttsx3.init()


playsound.playsound("eng.mp3")
