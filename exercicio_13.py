#city é igual a uma matriz
city =  [[0,15,30,5,12],[15,0,10,17,28],[30,10,0,3,11],[5,17,3,0,80],[12,28,11,80,0]]
#a váriavel n recebe o valor digitado pelo usuario
n = eval(input("Digite a quantidae de pares:\n"))
#a váriavel x é igual a 0
x = 0
#a váriavel i é igual a 0
i = 0
#a váriavel j é igual a 0
j = 0
#a váriavel soma é igual a 0
soma = 0
#d1 é igual a vetor
d1 = []
#d2 é igual a vetor
d2 = []
#enquanto x for menor que n
while x < n:
    #n1 recebe o valor digitado pelo usuario
    n1 = eval(input("Digite o valor:\n"))
    #é inserido no vetor d1 na posição x e o  valor n1
    d1.insert(x,n1)
    #n2 recebe o valor digitado pelo usuario
    n2 = eval(input("Digite outro valor:\n"))
    #é inserido no vetor d2 na posição x e o  valor n2
    d2.insert(x,n2)
    #i recebe d1 na posição x
    i = d1[x]
    #j recebe d1 na posição x
    j = d2[x]
    #soma recebe soma mais matriz city na posição n1 mais n2
    soma = soma + city[n1][n2]
    #x recebe mais 1
    x += 1
#printa o total que é iqual a váriavel soma
print("Total = "+str(soma))