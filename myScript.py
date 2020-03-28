# Import the required module for text
# to speech conversion
import playsound
from gtts import gTTS

# This module is imported so that we can
# play the converted audio
import os
import datetime
import time



# The text that you want to convert to audio
mytext = 'Welcome'
eventName = ""
profName = ""
location = ""
textToSpeech = "" 

os.chdir("F:\\GoogleCalendarPython")
# Language in which you want to convert
language = 'en'
i = 1



with open("events.txt", 'r') as f:
    data = f.readlines()

for line in data:
    mytext = line
    #       2020-03-30T15:30:00+05:30 #AI ML# $prof - Dinesh Kumar Baghel$ @C- 217@
    slot = mytext[:mytext.find(' ')]
    eventName = mytext[mytext.find('#')+1:mytext.rfind('#')]
    profName = mytext[mytext.find('$')+1:mytext.rfind('$')]
    location = mytext[mytext.find('@')+1:mytext.rfind('@')]

    if profName == mytext and location == mytext:
        pass
    else:
        if profName.find('#') < 0:
            textToSpeech = "Sir, there is  an upcoming event {0} Lecture, by {1}".format(eventName, profName)
        elif location.find('#') < 0:
            textToSpeech = "Sir, there is  an upcoming event {0}, Lecture, by {1}, at {2}".format(eventName, profName, location)
        else:
            textToSpeech = "Sir, there is  an upcoming event {0},".format(eventName)
    timefrag = slot.split('+')
    until = timefrag[0]
    playtime = datetime.datetime.strptime(until, '%Y-%m-%dT%H:%M:%S')
    #playtime = datetime.datetime.strptime('2020-03-28T00:31:00', '%Y-%m-%dT%H:%M:%S')

    while playtime > datetime.datetime.now():
        time.sleep(1)
        print (playtime - datetime.datetime.now())

    #print(playtime)
    #print(mytext)
    


    myobj = gTTS(text=textToSpeech, lang=language, slow=False)

    myobj.save("welcome" +str(i) + ".mp3") 
    

    playsound.playsound("welcome" + str(i) + ".mp3", True)

    i += 1
        
        




