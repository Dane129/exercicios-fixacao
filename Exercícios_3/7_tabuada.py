# Solicita ao usuário para inserir um número de 1 a 10
while True:
    try:
        N = int(input("Digite um número de 1 a 10: "))
        if 1 <= N <= 10:
            break
        else:
            print("Número fora do intervalo permitido. Tente novamente.")
    except ValueError:
        print("Por favor, insira um número válido.")

# Calcula e imprime a tabuada de N de 0 a 10
for i in range(11):
    resultado = i * N
    print(f"{i} x {N} = {resultado}")
