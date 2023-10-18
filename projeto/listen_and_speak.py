import speech_recognition as speechRecog
from playsound import playsound
from gtts import gTTS
import os
import pyttsx3


class ListenAndSpeak:
    def __init__(self, termSearch):
        self.termSearch = termSearch
     
        
    recognition = speechRecog.Recognizer()
    
   

    def listenF(self):
        print("ATNTES   with speechRecog")
        with speechRecog.Microphone() as source:
            print("DEPOIS   with speechRecog")
            try:
                print("Diga algo")

                audio = self.recognition.listen(source)
                print("DEPOIS   audio = self.recognition.listen(source)")

                

                text = self.recognition.recognize_google(audio, language="pt-BR")
             
                print("Você disse: " + text.capitalize())
                return text
            
            except FileNotFoundError:
                print("error Erro na captura da fala em [ListenAndSpeak/listenF]!")
                return {"error": "Erro na captura da fala em [ListenAndSpeak/listenF]!"}
                

         

    def speakF(self):
        try:
            # tts = gTTS(self.termSearch, lang="pt-BR", slow=False)

            # audio_file = os.path.dirname(__file__) + "audio.mp3"

            # tts.save(audio_file)

            # playsound(audio_file)
            engine = pyttsx3.init()
            engine.say(self.termSearch)
            engine.runAndWait()
            engine.stop()
        
        except FileNotFoundError:
                return {"error": "Erro na captura da fala em [ListenAndSpeak/speakF]!"}

        