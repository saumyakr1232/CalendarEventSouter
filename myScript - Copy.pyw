#version 2.1
# Import the required module for text
# to speech conversion
from gtts import gTTS

import urllib.request


# This module is imported so that we can
# play the converted audio\
import playsound
import os
import datetime
import time
import threading
# this module is imported to get/refresh event list from google calendar
import quickstart


def refreshListOfEvents():
    """ get/refresh event list from google calendar
        every 30 sec
    """
    while (True):
        global connected
        connected = connect()
        if(connected):
            try:
                quickstart.main()  # refresh events file
                global data
                data = readFile()  # update data (event list)
                time.sleep(30)
            except:
                print(
                    "Unable to Refresh events some error occured while getting events from google")
                time.sleep(10)
        else:
            time.sleep(10)
            print("Check your internet connection")


def readFile():
    """ read events file and create and return a list of events """
    global data
    with open("events.txt", 'r') as f:
        data = f.readlines()
    return data


def genrateMessage(mytext, profName, location, eventName):
    """ Genrate Message to speak """

    if profName == mytext and location == mytext:
        pass
    else:
        if profName.find('#') < 0:
            textToSpeech = "सर, there is  an upcoming event {0} Lecture, by {1}".format(
                eventName,
                profName,
            )
        elif location.find('#') < 0:
            textToSpeech = "सर, there is  an upcoming event {0}, Lecture, by {1}, at {2}".format(
                eventName,
                profName,
                location,
            )
        else:
            textToSpeech = "सर, there is  an upcoming event {0},".format(
                eventName,
            )
    return textToSpeech


def genratePlayTime(mytext):
    """ genrate a datetime object """
    slot = mytext[:mytext.find(' ')]
    timefrag = slot.split('+')
    until = timefrag[0]
    playtime = datetime.datetime.strptime(until, '%Y-%m-%dT%H:%M:%S')
    return playtime


def playSound(textToSpeech):
    """ play the message """
    obj = gTTS(text=textToSpeech, slow=False, lang='hi')
    obj.save('eng.mp3')
    playsound.playsound("eng.mp3")


def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False


def main():
    """ voice Notification for events from  google calendar
        updates every 30 secs"""

    # The text that you want to convert to audio
    mytext = 'Welcome'
    eventName = ""
    profName = ""
    location = ""
    textToSpeech = ""
    checked = False
    os.chdir("F:\\GoogleCalendarPython")
    # Language in which you want to convert
    language = 'hi'

    global data
    data = readFile()

    for line in data:
        mytext = line
        #       2020-03-30T15:30:00+05:30 #AI ML# $prof - Dinesh Kumar Baghel$ @C- 217@

        eventName = mytext[mytext.find('#')+1:mytext.rfind('#')]
        profName = mytext[mytext.find('$')+1:mytext.rfind('$')]
        location = mytext[mytext.find('@')+1:mytext.rfind('@')]

        textToSpeech = genrateMessage(mytext, profName,  location, eventName)

        playtime = genratePlayTime(mytext)
        print(playtime)
        #playtime = datetime.datetime.strptime('2020-03-28T15:59:00', '%Y-%m-%dT%H:%M:%S')

        while playtime > datetime.datetime.now():
            checked = True
            time.sleep(1)
            print(playtime - datetime.datetime.now())
            for line in data:
                mytext = line
                playtime2 = genratePlayTime(mytext)
                if playtime2 < playtime and playtime2 > datetime.datetime.now():
                    playtime = playtime2
                    eventName = mytext[mytext.find('#')+1:mytext.rfind('#')]
                    profName = mytext[mytext.find('$')+1:mytext.rfind('$')]
                    location = mytext[mytext.find('@')+1:mytext.rfind('@')]

                    textToSpeech = genrateMessage(
                        mytext, profName, location, eventName)

                else:
                    continue

        if (checked):
            playSound(textToSpeech)


if __name__ == "__main__":
    connected = connect()
    if(connected):
        quickstart.main()
    else:
        print("No internet connection available")
    data = []

    threadRefresh = threading.Thread(target=refreshListOfEvents, daemon=True)
    threadRefresh.start()
    main()
