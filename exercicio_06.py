#váriavel x = 0
x = 0
#váriavel altura = 0
altura = 0
#enquanto x for menor que 21
while x < 21:
    #a váriavel dado recebe o valor digitado pelo usuario
    dado = eval(input("Digite sua altura: \n"))
    #a variavel altura recebe o valor da altura mais o valor digitado pelo usuario
    altura = altura + dado
    #x é igual a mais 1
    x += 1
    #Se x for igual a 20
    if x == 20:
      #media será igual a altura dividido por 20
      media = altura / 20
      #printa que a media das alturas é igual a váriavel media
      print("Media = "+str(media))  
