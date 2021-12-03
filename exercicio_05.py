#A váriavel sexo recebe m ou f
sexo = input("Digite seu sexo\nm - masculino\nf - feminino\n")
#A váriavel altura recebe o dado informado pelo usuario
altura = eval(input("Digite a sua altura: \n"))
#Se sexo for igual a m
if sexo == 'm':
    #a váriavel pesoideal será igual a 72.7 vezes a altura, menos 58
    pesoideal = (72.7 * altura) - 58
    #printa que o peso ideal é igual a váriavel peso ideal
    print("Seu peso ideal é: "+str(pesoideal))
#Se sexo for igual a f
elif sexo == 'f':
    #a váriavel pesoideal será igual a 62.1 vezes a altura, menos 44.7
    pesoideal = (62.1 * altura) - 44.7
    #printa que o peso ideal é igual a váriavel peso ideal
    print("Seu peso ideal é: "+str(pesoideal))
#Senão
else:
    #printa que o sexo não foi encontrado
    print("Sexo não encontrado")