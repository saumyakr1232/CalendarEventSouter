from gtts import gTTS
import voic
import pyttsx3


eng = "सर, शशांक राजपूत द्वारा एक आगामी घटना समानांतर  व्याख्यान है "
obj = gTTS(text=eng, slow=False, lang='hi')
obj.save('eng.mp3')


# engine.setProperty('rate', 120)
# engine.say(eng)
# engine.runAndWait()

# engine = pyttsx3.init()


speak = wincl.Dispatch('SAPI.SpVoice')
speak.Speak(eng)
