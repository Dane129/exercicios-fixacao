algoritmo "semnome"
// Fun��o :
// Autor :
// Data : 14/10/2023
// Se��o de Declara��es 
var
x1, x2, y1, y2, p1, p2, q1, q2, vp: real
inicio
// Se��o de Comandos
escreva("Escreva o primeiro par /")
escreva("Digite x: ")
leia(x1)
escreva("Digite y: ")
leia(y1)
escreva("Escreva o segundo par /")
escreva("Digite x: ")
leia(x2)
escreva("Digite y: ")
leia(y2)
p1 <- x1 - x2
p2 <- y1 - y2
q1 <- p1 ^ 2
q2 <- p2 ^ 2
vp <- RAIZQ (q1 + q2)
escreva("A dist�ncia ser� de: ", vp)
fimalgoritmo
