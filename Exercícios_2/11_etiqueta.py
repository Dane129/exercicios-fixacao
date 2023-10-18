preco = float(input('Digite o valor da etiqueta: '))
forma_pagamento = input('Qual a forma de pagamento? a vista dinheiro, a vista cartão, duas vezes sem juros, duas com juros ')

if forma_pagamento == 'a vista dinheiro':
    desconto = preco*0.10
    preco = preco - desconto
elif forma_pagamento == 'a vista cartão':
    desconto = preco*0.15
    preco = preco - desconto
elif forma_pagamento == 'duas vezes sem juros':
    preco = preco
elif forma_pagamento == 'duas com juros':
    juros = preco*0.10
    preco = preco + juros

print(forma_pagamento, preco)