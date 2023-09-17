from month import Month

monthList = [
    Month("Janeiro", 0, 1),
    Month("Fevereiro", 0, 2),
    Month("Março", 0, 3),
    Month("Abril", 0, 4),
    Month("Maio", 0, 5),
    Month("Junho", 0, 6),
    Month("Julho", 0, 7),
    Month("Agosto", 0, 8),
    Month("Setembro", 0, 9),
    Month("Outubro", 0, 10),
    Month("Novembro", 0, 11),
    Month("Dezembro", 0, 12),
]


sumTemperatures = 0


for month in monthList:
    month.setAverageTemperature(
        int(input("Informe a temperatura média do mês de " + month.name + ": "))
    )
    sumTemperatures += month.averageTemperature


averageTemperatures = sumTemperatures / monthList.__len__()

print("############### TEMPERATURA MÉDIA ANUAL = ", averageTemperatures ," ###############")
print("----------------------------------------------------------------")
print("############### TEMPERATURAS À CIMA DA MÉDIA ANUAL ###############")

for month in monthList:
    if month.averageTemperature > averageTemperatures:
        month.printMonth()
