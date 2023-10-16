pessoa_altura = float(input('Digite sua altura: '))
pessoa_sombra = float(input('Digite sua sombra: '))

sombra_predio = float(input('Digite o comprimento da sombra do prédio: '))

altura_predio = (pessoa_altura / pessoa_sombra) * sombra_predio
altura_predio = round(altura_predio, 2)

print('A altura do prédio será de:', altura_predio, " metros")
