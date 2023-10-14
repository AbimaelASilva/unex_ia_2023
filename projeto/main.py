import speech_recognition as speechRecog
from playsound import playsound
from gtts import gTTS
import os

from consume_API_repository import ConsumeAPIRepository


recognition = speechRecog.Recognizer()



with speechRecog.Microphone() as source:
    print("Diga algo")

    audio = recognition.listen(source)

    text = recognition.recognize_google(audio, language="pt-BR")
 

    try:
        print("Você disse: " + text.capitalize())
    except FileNotFoundError:
        print("Não foi possível compreender o audio")

    tts = gTTS(text, lang="pt-BR", slow=False)

    audio_file = os.path.dirname(__file__) + "audio.mp3"

    tts.save(audio_file)

    playsound(audio_file)

    os.remove(audio_file)

    ConsumeAPIRepository()
