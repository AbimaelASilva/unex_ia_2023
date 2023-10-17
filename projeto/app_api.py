import requests
from flask import Flask, jsonify, request
from listen_and_speak import ListenAndSpeak


# url = "https://www.omdbapi.com/?s=batman&apikey=9329b862"
prefixUrl = "https://www.omdbapi.com/?s="

key = "9329b862"


app = Flask(__name__)




@app.route("/enableListening")
def enableListening():

    try:
        termSearch = ListenAndSpeak("").listenF()

        splitedText = termSearch.split("Ok unex buscar por ")

        response= getMovies(splitedText[1])



      #  print("TERMO RETORNADO DO MICROFONE "+termSearch)
        print("TERMO SEPARADO "+splitedText[1])

        ListenAndSpeak("Entendi, buscando por: "+splitedText[1]).speakF()

        

        #return {"retorno": "retorno de enableListening"}
        return response
        
    except FileNotFoundError:
      return {"error": "Erro na captura da fala em [enableListening]!"}

    



#@app.route("/getMovies")
def getMovies(termSearch):

    url = prefixUrl + termSearch + "&apikey=" + key

   
    print("URL COMPLETA: " + url)
    
    resultado = requests.get(url)
   
    print(resultado)
   # print(resultado.json())

    return resultado.text


app.run(port=5000, host="localhost", debug=True)
