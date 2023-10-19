import random 

sequencia = random.sample(range(101), 10)

intervalos = [(0, 25), (26, 50), (51, 75), (76, 100)]

contadores = [0] * len(intervalos)

for numero in sequencia:
    for i, (li, ls) in enumerate(intervalos):
        if li <= numero <= ls:
            contadores[i] += 1

for i, (li, ls) in enumerate(intervalos):
    print(f'numeros entre {li} e {ls}: {contadores[i]}')