numeros = []

for i in range(3):
    numero = int(input('Digite um número: '))
    numeros.append(numero)

numeros.sort(reverse=True)

print(numeros)