algoritmo "semnome"
// Fun��o :
// Autor :
// Data : 15/10/2023
// Se��o de Declara��es 
var
conta, carlos, andre, felipe, resto: real
inicio
// Se��o de Comandos
escreva("Escreva o valor da conta: ")
leia(conta)
conta <- conta/3
carlos <- conta - 1
andre <- conta - 1
resto <- conta - carlos + andre
felipe <- resto + 2 - 0.31
escreva("Carlos pagar� ", carlos:1:0, " Andr� pagar� ", andre:1:0, " Felipe pagar� ", felipe:1:2)
fimalgoritmo
