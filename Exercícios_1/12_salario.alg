algoritmo "semnome"
// Fun��o :
// Autor :
// Data : 15/10/2023
// Se��o de Declara��es 
var
salario, aumento, desconto, salariofinal, sal: real
inicio
// Se��o de Comandos
escreva("Escreva o sal�rio: ")
leia(salario)
aumento <- salario*0.15
salario <- aumento+salario
desconto <- aumento*0.08
salariofinal <- salario-desconto
sal <- salario - aumento
escreva("O novo sal�rio ser�: ", salariofinal, "O inicial �: ", sal)
fimalgoritmo
