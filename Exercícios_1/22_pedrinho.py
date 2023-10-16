moeda1 = float(input('Digite o valor das moedas de 1 centavo: '))
moeda2 = float(input('Digite o valor das moedas de 5 centavos: '))
moeda3 = float(input('Digite o valor das moedas de 10 centavos: '))
moeda4 = float(input('Digite o valor das moedas de 25 centavos: '))
moeda5 = float(input('Digite o valor das moedas de 50 centavos: '))
moeda6 = float(input('Digite o valor das moedas de 1 real: '))

moeda1 = moeda1 * 0.01
moeda2 = moeda2 * 0.05
moeda3 = moeda3 * 0.10
moeda4 = moeda4 * 0.25
moeda5 = moeda5 * 0.50
moeda6 = moeda6 * 1.00

total = moeda1 + moeda2 + moeda3 + moeda4 + moeda5 + moeda6

print('Seu cofrinho possui:', total, " reais")
