import speech_recognition as speechRecog
from playsound import playsound
import pyttsx3
from gtts import gTTS
import os


recognition = speechRecog.Recognizer()
engine = pyttsx3.init()


with speechRecog.Microphone() as source:
    print("Diga algo")

    audio = recognition.listen(source)

    text = recognition.recognize_google(audio, language="pt-BR")

    # engine.say(text)

    # engine.runAndWait()

    try:
        print("Você disse: " + text.capitalize())
    except:
        print("Não foi possível compreender o audio")

    tts = gTTS(text, lang="pt-BR", slow=False)

    audio_file = os.path.dirname(__file__) + "audio.mp3"

    tts.save(audio_file)

    playsound(audio_file)

    os.remove(audio_file)
