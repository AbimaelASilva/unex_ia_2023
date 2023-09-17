import random

from number_controller import NumberController

randomNumber = 0

numberList = [NumberController(i+1, 0) for i in range(6)]

sum = 0
for count in range(1, 101):
      randomNumber = random.randint(1,6)

      for numberController in numberList:
            if(randomNumber ==numberController.number):
                  repetitions = numberController.getRepetitions() +1
                  numberController.setRepetitions(repetitions) 

print("############### SIMULAÇÃO DE LANÇÃMENTO DE DADOS/INFORMAÇÕES ###############")

for numberController in numberList:
      numberController.printNumber()


