algoritmo "semnome"
// Função :
// Autor :
// Data : 15/10/2023
// Seção de Declarações 
var
conta, carlos, andre, felipe, resto: real
inicio
// Seção de Comandos
escreva("Escreva o valor da conta: ")
leia(conta)
conta <- conta/3
carlos <- conta - 1
andre <- conta - 1
resto <- conta - carlos + andre
felipe <- resto + 2 - 0.31
escreva("Carlos pagará ", carlos:1:0, " André pagará ", andre:1:0, " Felipe pagará ", felipe:1:2)
fimalgoritmo
