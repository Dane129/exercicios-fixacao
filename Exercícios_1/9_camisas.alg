algoritmo "semnome"
// Função :
// Autor :
// Data : 14/10/2023
// Seção de Declarações 
var
camisapequena, camisamedia, camisagrande, valorfinal: real
inicio
// Seção de Comandos
escreva("Quantas camisas pequenas? ")
leia(camisapequena)
escreva("Quantas camisas médias? ")
leia(camisamedia)
escreva("Quantas camisas grandes? ")
leia(camisagrande)
camisapequena <- camisapequena * 10
camisamedia <- camisamedia * 12
camisagrande <- camisagrande * 15
valorfinal <- camisapequena + camisamedia + camisagrande
escreva("O total de tudo dará: ", valorfinal)
fimalgoritmo
