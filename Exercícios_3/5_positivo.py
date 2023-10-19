# Sequência de números
import random

sequencia = random.sample(range(101), 10)

# Lista para armazenar números pares e ímpares
numeros_pares = []
numeros_impares = []

# Separa números pares e ímpares
for numero in sequencia:
    if numero % 2 == 0:
        numeros_pares.append(numero)
    else:
        numeros_impares.append(numero)

# Calcula a soma e a média dos números pares
soma_pares = sum(numeros_pares)
media_pares = soma_pares / len(numeros_pares) if len(numeros_pares) > 0 else 0

# Calcula a soma e a média dos números ímpares
soma_impares = sum(numeros_impares)
media_impares = soma_impares / len(numeros_impares) if len(numeros_impares) > 0 else 0

media_pares = round(media_pares, 2)
media_impares = round(media_impares, 2)

# Soma os elementos das listas de números pares e ímpares
soma_total = sum(numeros_pares) + sum(numeros_impares)

# Calcula a média geral
numero_total = len(numeros_pares) + len(numeros_impares)
media_geral = soma_total / numero_total if numero_total > 0 else 0

# Imprime números pares e ímpares, soma e média
print("Números pares:", numeros_pares)
print("Números ímpares:", numeros_impares)
print("Soma dos números pares:", soma_pares)
print("Média dos números pares:", media_pares)
print("Soma dos números ímpares:", soma_impares)
print("Média dos números ímpares:", media_impares)
print("Média geral: ", media_geral)
