import requests
from flask import Flask, jsonify, request
from listen_and_speak import ListenAndSpeak


# url = "https://www.omdbapi.com/?s=batman&apikey=9329b862"
prefixUrl = "https://www.omdbapi.com/?s="
termSearch = ""
key = "9329b862"


app = Flask(__name__)


def urlComplete():
    return prefixUrl + termSearch + "&apikey=" + key


@app.route("/enableListening")
def enableListening():

    try:
        termSearch = ListenAndSpeak().listenF()

        print("TERMO RETORNADO DO MICROFONE "+termSearch)

        return {"retorno": "retorno de enableListening"}
        
    except FileNotFoundError:
      return {"error": "Erro na captura da fala em [enableListening]!"}

    



@app.route("/getMovies")
def getMovies():
    url = urlComplete()
   
    print("URL COMPLETA: " + url)
    
    resultado = requests.get(url)
   
    print(resultado)
   # print(resultado.json())

    return resultado.text


app.run(port=5000, host="localhost", debug=True)
