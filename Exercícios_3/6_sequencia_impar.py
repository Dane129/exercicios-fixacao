import random

sequencia = random.sample(range(100, 201), 10)

numeros_impares = []

for numero in sequencia:
    if numero % 2 == 0 and numero % 3:
        numeros_impares.append(numero)

print(numeros_impares)