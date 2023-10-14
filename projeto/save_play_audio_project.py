import speech_recognition as speechRecog
from playsound import playsound
import pyaudio
import wave

recognition = speechRecog.Recognizer()

with speechRecog.Microphone() as source:
    print("Diga algo")

    audio = recognition.listen(source)

   
    text =  recognition.recognize_google(audio, language = 'pt-BR')
      

    # Salve o áudio em um arquivo WAV
    with open("captured_audio.wav", "wb") as file:
        file.write(audio.get_wav_data())

        # Reproduza o áudio usando pyaudio
    def play_audio(filename):
        chunk = 1024
        wf = wave.open(filename, 'rb')
        p = pyaudio.PyAudio()

        stream = p.open(
            format=p.get_format_from_width(wf.getsampwidth()),
            channels=wf.getnchannels(),
            rate=wf.getframerate(),
            output=True
        )

        data = wf.readframes(chunk)
        while data:
            stream.write(data)
            data = wf.readframes(chunk)

        stream.stop_stream()
        stream.close()
        p.terminate()

    # Reproduza o áudio capturado
    play_audio("captured_audio.wav")

    try:
        print("Você disse: "+ text.capitalize())
    except: 
        print("Não foi possível compreender o audio")