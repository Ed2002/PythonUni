#num é igual a um vetor
num = []
#a variavel x é igual a 0
x = 0
#a variavel ma é igual a 0
ma = 0
#a variavel me é igual a 99
me = 99
#enquanto x for menor igual a 5
while x <= 5:
    #num recebe o valor digitado pelo usuario
    num = eval(input("Digite um número: \n"))
    #Se num for maior que ma
    if num > ma:
        #ma recebe o valor de num
        ma = num
    #Se num for menor que me    
    elif num < me:
        #me for igual a num
        me = num
    #x recebe mais 1
    x += 1
#Se x for igual a 6
if x == 6:
    #printa o maior número com a váriavel ma e o menor com a váriavel me
    print("O Maior número é = "+str(ma)+"\nO Menor número é = "+str(me))