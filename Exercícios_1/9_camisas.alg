algoritmo "semnome"
// Fun��o :
// Autor :
// Data : 14/10/2023
// Se��o de Declara��es 
var
camisapequena, camisamedia, camisagrande, valorfinal: real
inicio
// Se��o de Comandos
escreva("Quantas camisas pequenas? ")
leia(camisapequena)
escreva("Quantas camisas m�dias? ")
leia(camisamedia)
escreva("Quantas camisas grandes? ")
leia(camisagrande)
camisapequena <- camisapequena * 10
camisamedia <- camisamedia * 12
camisagrande <- camisagrande * 15
valorfinal <- camisapequena + camisamedia + camisagrande
escreva("O total de tudo dar�: ", valorfinal)
fimalgoritmo
