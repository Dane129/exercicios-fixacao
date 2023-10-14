algoritmo "semnome"
// Função :
// Autor :
// Data : 14/10/2023
// Seção de Declarações 
var
pao, broa, soma, poupanca: real
inicio
// Seção de Comandos
escreva("Digite a quantidade de pães vendidos: ")
leia(pao)
pao <- pao * 0.12
escreva("Digite a quantidade de broas vendidas: ")
leia(broa)
broa <- broa * 1.50
soma <- pao + broa
escreva("Você arrecadou", soma," reais no total")
poupanca <- soma * 0.10
escreva(" e deve guardar na poupança", poupanca," reais")
fimalgoritmo
