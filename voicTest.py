from gtts import gTTS
import win32com.client as wincl
import pyttsx3



eng = "Sir there is an upcoming event parallel uviverse lecture by shashank rajpoot at galgotias university"
obj = gTTS(text=eng, slow=False, lang='bh')
obj.save('eng.mp3')


# engine.setProperty('rate', 120)
# engine.say(eng)
# engine.runAndWait()

# engine = pyttsx3.init()


speak = wincl.Dispatch('SAPI.SpVoice')
speak.Speak(eng)
