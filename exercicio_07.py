#váriavel negativo é igual a 0
negativo = 0
#váriavel r é igual a 1
r = 1
#enquanto r for diferente de 0
while r != 0:
    #a váriavel num recebe o valor digitado pelo usuario
    num = eval(input("Digite um número"))
    #a váriavel r recebe ou o valor 0 pra sair ou outro valor para continuar
    r = eval(input("Digite 1 para continuar ou 0 para sair\n"))
    #Se num for menor que 0
    if num < 0:
        #negativo é igual a mais 1
        negativo += 1    
#Se r for igual a 0
if r == 0:
    #printa o que o total de números negativos é igual a váriavel negativo
    print("Total de números negativos = "+str(negativo))
    