algoritmo "semnome"
// Função :
// Autor :
// Data : 14/10/2023
// Seção de Declarações 
var
n1, n2, n3, nf, np: real
inicio
// Seção de Comandos
escreva("Escreva a primeira nota: ")
leia(n1)
escreva("Escreva a segunda nota: ")
leia(n2)
escreva("Escreva terceira nota: ")
leia(n3)
n1 <- n1 * 1
n2 <- n2 * 2
n3 <- n3 * 3
nf <- n1 + n2 + n3
np <- nf / 6
escreva("A nota ponderada será: ", np:3:2)
fimalgoritmo
