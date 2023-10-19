alturas = []

for i in range(15):
    altura = float(input('Digite a sua altura: '))
    alturas.append(altura)

print('A menor altura é: ', min(alturas))
print('A maior altura é: ', max(alturas))