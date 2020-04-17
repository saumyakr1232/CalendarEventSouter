import pyttsx3
converter = pyttsx3.init()

voices = converter.getProperty('voices')

for voice in voices:
	# to get the info. about various voices in our PC
	print("Voice:")
	print("ID: %s" % voice.id)
	print("Name: %s" % voice.name)
	print("Age: %s" % voice.age)
	print("Gender: %s" % voice.gender)
	print("Languages Known: %s" % voice.languages)


#HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0
#HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0
#"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"


# Voice:
# ID: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0
# Name: Microsoft Hazel Desktop - English(Great Britain)
# Age: None
# Gender: None
# Languages Known: []
# Voice:
# ID: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0
# Name: Microsoft Zira Desktop - English(United States)
# Age: None
# Gender: None
# Languages Known: []

id_male = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0"
id_female = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"


voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"

# Use female voice
# converter.setProperty(
#     'voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0")

converter.setProperty('rate', 120)
voice = converter.getProperty('voice')
print()
print(voice)
for voice in voices:
   converter.setProperty('voice', voice.id)
   converter.say('The quick brown fox jumped over the lazy dog.')
converter.runAndWait()


