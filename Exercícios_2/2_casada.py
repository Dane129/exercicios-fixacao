nome = input('Qual é o seu nome? ')
sexo = input('Qual é o seu sexo? F ou M ')
estadocivil = input('Qual o seu estado civi? Solteira, Casada ou Outros ')

if sexo == 'F' and estadocivil == 'Casada':
    print('Quanto tempo está casada?')
else:
    print('')