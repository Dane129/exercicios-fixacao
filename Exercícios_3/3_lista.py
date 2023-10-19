lista = []

negativo = 0
positivo = 0
soma = 0

for i in range(6):
    listas = float(input("Digite um número: "))
    lista.append(listas)

total_elementos = len(lista)

for numero in lista:
    if numero < 0:
        negativo += 1
    elif numero > 0:
        positivo += 1

percentual_negativo = (negativo / total_elementos)*100
percentual_positivo = (positivo / total_elementos)*100

for numero in lista:
    soma += numero

soma = soma / 6
soma = round(soma, 2)

print('A contagem de números negativos é: ', negativo)
print('A contagem de números positivos é: ', positivo)
print('A média é: ', soma)
print('O percentual negativo é de: {:.2f}%' .format(percentual_negativo))
print('O percentual positivo é de: {:.2f}%' .format(percentual_positivo))