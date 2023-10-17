nascimento = int(input('Digite o seu ano de nascimento: '))
ano_atual = 2023

idade = ano_atual - nascimento
meses = idade * 12
dias = meses * 30
semanas = dias / 7
semanas = round(semanas, 2)

print('Sua idade é: ', idade)
print('Sua idade em meses é:', meses)
print('Sua idade em dias é:', dias)
print('Sua idade em semanas é: ', semanas)

