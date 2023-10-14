import requests

# # Captura o período a ser consultado, formato AAAAMM
# mesAno = 202008
# # Captura o código IBGE
# codigoIbge = 3550308
# # Valor fixo na consulta, já que o serviço retorna somente uma página
# pagina = 1
# # Cria o dicionário com as informações capturadas
# params = {"mesAno":mesAno, "codigoIbge":codigoIbge, "pagina":pagina}

# headers = {"chave-api-dados" : "cole sua chave aqui"}

url = "https://www.omdbapi.com/?s=batman&apikey=9329b862"

#chamando a função e salvando seu resultado



class ConsumeAPIRepository:
    def getMovies():
        resultado = requests.get(url)
        print(resultado)
        print(resultado.json())
