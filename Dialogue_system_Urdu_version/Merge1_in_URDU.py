# import pyttsx3
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import os

def takecommand():
    r = sr.Recognizer()
    user=""
    with sr.Microphone()as source:
        print("Listening")
        r.pause_threshold = 1
        audio =r.listen(source,timeout=1,phrase_time_limit=5)
    try:
        print("Recognizing")
        urdu_text =r.recognize_google(audio,language= 'ur')
        print(urdu_text)
        return urdu_text

    except Exception as e:
        speak("you have not said any thing......... ")
        return
    return urdu_text
def speak(urdu_text):
    audio = gTTS(text=urdu_text, lang="ur")
    audio.save("textaudio.mp3")
    playsound("textaudio.mp3")
    #os.remove(filename)
for i in range(10):
    print("speak please")
    urdu_text = takecommand()
    speak(urdu_text)

#Translation
eng_text="The centre is designed to become a leading hub of innovation, scientific research, knowledge transfer of the local economy and training in the area of Artificial Intelligence(AI) and its closely associated fields.NCAI, divided further into two labs with cutting edge technology.First one is Smart City Lab and second one is Neuro Computation Lab"

from googletrans import Translator
translator = Translator()
translation = translator.translate(eng_text, dest="ur")
print(translation.text)
speak(translation.text)