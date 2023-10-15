algoritmo "semnome"
// Função :
// Autor :
// Data : 15/10/2023
// Seção de Declarações 
var
numero, centena, dezena, unidade: real
inicio
// Seção de Comandos
escreva("Digite três números: ")
leia(numero)
se numero >= 111 entao
dezena <- numero/10
centena <- numero/100
unidade <- numero
escreva(centena, " centenas", dezena, " dezenas", unidade, " unidades")
fimse
fimalgoritmo

