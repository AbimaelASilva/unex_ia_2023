class Month:
    def __init__(
        self,
        name,
        averageTemperature,
        monthNumber,
    ):
        self.name = name
        self.averageTemperature = averageTemperature
        self.monthNumber = monthNumber

#Setters
    def setMonthName(self, name):
        self.name = name

    def setAverageTemperature(self, averageTemperature):
        self.averageTemperature = averageTemperature
    
    def setMonthNumber(self, monthNumber):
        self.name = monthNumber

#Getters
    def getMonthName(self):
        return self.name

    def getAverageTemperature(self):
        return self.averageTemperature

    def getMonthNumber(self):
        return self.monthNumber


    def printMonth(self):
        print("----------------------------------------------------------------")
        print("Temperatura média: ", str(self.averageTemperature))
        print(self.monthNumber," -", self.name)
