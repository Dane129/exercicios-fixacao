salario = float(input('Digite o salário atual do funcionário: '))

minimo = 1320

calculo = salario / minimo

calculo = round(calculo, 2)
print('Você recebe:', calculo, 'salários mínimos')
