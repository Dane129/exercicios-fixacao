import math

v1 = int(input('Digite o primeiro valor do cateto: '))
v2 = int(input('Digite o segundo valor do cateto: '))

v1 = v1 ** 2
v2 = v2 ** 2

total = v1 + v2

raiz = math.sqrt(total)

print('O valor da hipotenusa será: ', raiz)
