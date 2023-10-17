import speech_recognition as speechRecog
from playsound import playsound
from gtts import gTTS
import os


class ListenAndSpeak:
    def __init__(self, termSearch):
        self.termSearch = termSearch
     
    recognition = speechRecog.Recognizer()
   

    def listenF(self):
        with speechRecog.Microphone() as source:
            try:
                print("Diga algo")

                audio = self.recognition.listen(source)

                text = self.recognition.recognize_google(audio, language="pt-BR")
                print("Você disse: " + text.capitalize())
                return text
            
            except FileNotFoundError:
                return {"error": "Erro na captura da fala em [ListenAndSpeak/listenF]!"}
                

         

    def speakF(self):
        try:
            tts = gTTS(self.termSearch, lang="pt-BR", slow=False)

            audio_file = os.path.dirname(__file__) + "audio.mp3"

            tts.save(audio_file)

            playsound(audio_file)
        
        except FileNotFoundError:
                return {"error": "Erro na captura da fala em [ListenAndSpeak/speakF]!"}

        