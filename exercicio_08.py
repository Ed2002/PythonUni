#valores é um vetor
valores = list()
#a váriavel sp é igual a 0
sp = 0
#a váriavel si é igual a 0
si = 0
#para cont em um vetor de 0 até 99
for cont in range(0, 99):
    #Se conte tiver o resto igual a dois cont é um número par 
    if cont % 2 == 0:
        #sp recebe sp mais cont
        sp = sp + cont
    #Senão cont pe um número impar
    else:
        #si recebe si mais cont
        si = si + cont  
#printa a soma dos numeros pares sp e dos impares si
print("\nSoma dos números pares: "+str(sp)+"\nSoma dos números impares: "+str(si))