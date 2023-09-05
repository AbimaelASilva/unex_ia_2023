print("VAMOS CALCULAR O SEU IMC?")

print("Qual seu peso?")

weight = int(input())

print("Qual sua altura(em metros, por exemplo: 1.75)?")

height = float(input())

imc = weight/(height * height)


print("SEU ÍNDICE DE MASSA CORPÓERA(IMC) É: ",imc)

if imc <= 18.5:
    print("Você esta á baixo do peso!")
elif imc > 18.5 and imc <= 24.9:
    print("parabéns seu peso esta normal!")
elif imc > 24.9 and imc <= 29.9:
    print("Cuidado. Você esta com obesidade grau I!")
elif imc > 29.9 and imc <= 39.9:
    print("Atenção. Você esta com obesidade grau II!")
else:
    print("URGENTE. Você esta com obesidade grau IIi OU MÓRBIDA!")
