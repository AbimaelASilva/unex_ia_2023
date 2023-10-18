import requests
from flask import Flask, jsonify, request
from listen_and_speak import ListenAndSpeak
from deep_translator import GoogleTranslator

import has_internet


# url = "https://www.omdbapi.com/?s=batman&apikey=9329b862"
prefixUrl = "https://www.omdbapi.com/?s="

key = "9329b862"


app = Flask(__name__)


@app.route("/enableListening")
def enableListening():
    hasInternet = True
    try:
        hasInternet = has_internet.has_internet()

        print(hasInternet)

        if hasInternet:
            termSearch = ListenAndSpeak("").listenF()

            if termSearch.__contains__("por "):
                splitedText = termSearch.split("por ")

                translatedText = GoogleTranslator(
                    source="portuguese", target="english"
                ).translate(splitedText[1])

                #  print("TERMO RETORNADO DO MICROFONE "+termSearch)
                print("TEXTO SEM TRADUZIR: " + splitedText[1])
                print("TEXTO TRADUZIDO: " + translatedText)

                response = getMovies(translatedText)

                ListenAndSpeak("Entendi, buscando por: " + splitedText[1]).speakF()

                return response
            else:
                print("ERRRO NO TEXTO DA VOZ")
                ListenAndSpeak("Desculpe, não comprendi o que deseja buscar.").speakF()
        else:
            print("====>Umm, acho que você esta sem conexão com a internet!")
            ListenAndSpeak(
                "Percebi que você pode esta sem conexão com a internet!"
            ).speakF()

    except FileNotFoundError:
        ListenAndSpeak(
            "Umm, me parece que você esta com algum problema de conexão com a internet."
        ).speakF()
        return {"error": "Erro na captura da fala em [enableListening]!"}


# @app.route("/getMovies")
def getMovies(termSearch):
    url = prefixUrl + termSearch + "&apikey=" + key

    print("URL COMPLETA: " + url)

    resultado = requests.get(url)

    print(resultado)
    # print(resultado.json())

    return resultado.text


app.run(port=5000, host="localhost", debug=True)
