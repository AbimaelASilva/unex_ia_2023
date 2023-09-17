class NumberController:
    def __init__(
        self,
        number,
        repetitions,
    ):
        self.number = number
        self.repetitions = repetitions

    # Setters
    def setNumber(self, number):
        self.number = number

    def setRepetitions(self, repetitions):
        self.repetitions = repetitions

    # Getters
    def getNumber(self):
        return self.number

    def getRepetitions(self):
        return self.repetitions

    def printNumber(self):
        print("\n")
        print("----------------------------------------------------------------")
        print("Número: ", str(self.number))
        print("Repetiu", self.repetitions, "vezes!")
