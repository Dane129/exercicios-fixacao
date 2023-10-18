humano = input('homem ou mulher? ')
h = float(input('Qual a sua altura? '))

if humano == 'homem':
    h = (72.7*h) - 58
else:
    h = (62.1*h) - 44.7

h = round(h, 2)

print(h)