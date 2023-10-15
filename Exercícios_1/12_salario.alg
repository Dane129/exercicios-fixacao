algoritmo "semnome"
// Função :
// Autor :
// Data : 15/10/2023
// Seção de Declarações 
var
salario, aumento, desconto, salariofinal, sal: real
inicio
// Seção de Comandos
escreva("Escreva o salário: ")
leia(salario)
aumento <- salario*0.15
salario <- aumento+salario
desconto <- aumento*0.08
salariofinal <- salario-desconto
sal <- salario - aumento
escreva("O novo salário será: ", salariofinal, "O inicial é: ", sal)
fimalgoritmo
