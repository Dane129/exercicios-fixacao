lata = float(input('Digite o número de latas de 350 ml que deseja comprar: '))
garrafa = float(input('Digite o número de garrafas de 600 ml que deseja comprar: '))
garrafa_2 = float(input('Digite o número de garrafas de 2 litros que deseja comprar: '))

lata = lata * 0.350
garrafa = garrafa * 0.600
garrafa_2 = garrafa_2 * 2.000
total = lata + garrafa + garrafa_2

print('A quantidade total de refrigerante será de: ', total)
