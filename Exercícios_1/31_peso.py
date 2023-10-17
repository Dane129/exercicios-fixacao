peso = float(input('Digite o seu peso aqui: '))

add = peso * 0.15
remove = peso * 0.20

peso1 = peso + add
peso2 = peso - remove

print('Seu peso caso engorde será de:', peso1, ' com 15% de acréscimo')
print('Seu peso caso emagreça será de:', peso2, ' com 20% de redução')
