algoritmo "semnome"
// Fun��o :
// Autor :
// Data : 14/10/2023
// Se��o de Declara��es 
var
pao, broa, soma, poupanca: real
inicio
// Se��o de Comandos
escreva("Digite a quantidade de p�es vendidos: ")
leia(pao)
pao <- pao * 0.12
escreva("Digite a quantidade de broas vendidas: ")
leia(broa)
broa <- broa * 1.50
soma <- pao + broa
escreva("Voc� arrecadou", soma," reais no total")
poupanca <- soma * 0.10
escreva(" e deve guardar na poupan�a", poupanca," reais")
fimalgoritmo
