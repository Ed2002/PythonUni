#váriavel letra recebe o valor digitado pelo usuário
letra = input("Digite algo: \n")
#Se letra for igual a A ou E ou I ou U
if letra == 'a' or letra == 'A' or letra == 'e' or letra == 'E' or letra == 'i' or letra == 'I' or letra == 'o' or letra == 'O' or letra == 'u' or letra == 'U':
    #printa Vogal
    print("Vogal")
#Senão
else:
    #printa Consoante
    print("Consoante")