algoritmo "semnome"
// Fun��o :
// Autor :
// Data : 15/10/2023
// Se��o de Declara��es 
var
numero, centena, dezena, unidade: real
inicio
// Se��o de Comandos
escreva("Digite tr�s n�meros: ")
leia(numero)
se numero >= 111 entao
dezena <- numero/10
centena <- numero/100
unidade <- numero
escreva(centena, " centenas", dezena, " dezenas", unidade, " unidades")
fimse
fimalgoritmo

