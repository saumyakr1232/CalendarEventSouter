# Import the required module for text
# to speech conversion
import pyttsx3
engine = pyttsx3.init()

# This module is imported so that we can
# play the converted audio
import os
import datetime
import time
import threading
import quickstart


def refresh():
    while (True):
        print("hii")
        quickstart.main()
        readFile()
        time.sleep(30)


def readFile():
    global data
    with open("events.txt", 'r') as f:
        data = f.readlines()


if __name__ == "__main__":
    # The text that you want to convert to audio
    mytext = 'Welcome'
    eventName = ""
    profName = ""
    location = ""
    textToSpeech = ""
    checked = False
    os.chdir("F:\\GoogleCalendarPython")
    # Language in which you want to convert
    language = 'en'
    i = 1
    threadRefresh = threading.Thread(target=refresh)
    threadRefresh.start()

    with open("events.txt", 'r') as f:
        data = f.readlines()

    for line in data:
        mytext = line
        #       2020-03-30T15:30:00+05:30 #AI ML# $prof - Dinesh Kumar Baghel$ @C- 217@

        eventName = mytext[mytext.find('#')+1:mytext.rfind('#')]
        profName = mytext[mytext.find('$')+1:mytext.rfind('$')]
        location = mytext[mytext.find('@')+1:mytext.rfind('@')]

        if profName == mytext and location == mytext:
            pass
        else:
            if profName.find('#') < 0:
                textToSpeech = "Sir, there is  an upcoming event {0} Lecture, by {1}".format(
                    eventName, profName)
            elif location.find('#') < 0:
                textToSpeech = "Sir, there is  an upcoming event {0}, Lecture, by {1}, at {2}".format(
                    eventName, profName, location)
            else:
                textToSpeech = "Sir, there is  an upcoming event {0},".format(
                    eventName)
        slot = mytext[:mytext.find(' ')]
        timefrag = slot.split('+')
        until = timefrag[0]
        playtime = datetime.datetime.strptime(until, '%Y-%m-%dT%H:%M:%S')
        print(playtime)
        #playtime = datetime.datetime.strptime('2020-03-28T15:59:00', '%Y-%m-%dT%H:%M:%S')

        while playtime > datetime.datetime.now():
            checked = True
            time.sleep(1)
            print(playtime - datetime.datetime.now())
            for line in data:
                mytext = line
                slot = mytext[:mytext.find(' ')]
                timefrag = slot.split('+')
                until = timefrag[0]
                playtime2 = datetime.datetime.strptime(
                    until, '%Y-%m-%dT%H:%M:%S')
                if playtime2 < playtime and playtime2 > datetime.datetime.now():
                    playtime = playtime2
                    eventName = mytext[mytext.find('#')+1:mytext.rfind('#')]
                    profName = mytext[mytext.find('$')+1:mytext.rfind('$')]
                    location = mytext[mytext.find('@')+1:mytext.rfind('@')]

                    if profName == mytext and location == mytext:
                        pass
                    else:
                        if profName.find('#') < 0:
                            textToSpeech = "Sir, there is  an upcoming event {0} Lecture, by {1}".format(
                                eventName, profName)
                        elif location.find('#') < 0:
                            textToSpeech = "Sir, there is  an upcoming event {0}, Lecture, by {1}, at {2}".format(
                                eventName, profName, location)
                        else:
                            textToSpeech = "Sir, there is  an upcoming event {0},".format(
                                eventName)
                else:
                    continue

        if (checked):
            engine.setProperty('rate', 120)
            engine.say(textToSpeech)
            engine.runAndWait()
            engine.stop()
