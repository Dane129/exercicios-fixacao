n1 = int(input('Digite a primeira nota: '))
n2 = int(input('Digite a segunda nota: '))
n3 = int(input('Digite a terceira nota: '))
me = int(input('Digite a média do exercício: '))

soma = ((n1 + (n2*2) + (n3*3) + me) / 7)

print(round(soma, 2))

if soma >= 9:
    print('A, Aprovado')
elif soma >= 7.5 and soma < 9:
    print('B, Aprovado')
elif soma >= 6 and soma < 7.5:
    print('C, Aprovado')
elif soma >= 4 and soma < 6:
    print('D, Reprovado')
elif soma < 4:
    print('E, Reprovado')
