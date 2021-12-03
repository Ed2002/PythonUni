#nome é igual a um vetor
nome = []
#nota é igual a um vetor
nota = []
#váriavel x é igual a 0
x = 0
#váriavel c é igual a 0
c = 0
#váriavel i é igual a 0
i = 0
#váriavel soma é igual a 0
soma = 0
#enquanto x for menor 51 
while x < 51:
    #a váriavel nm recebe o valor digitado pelo usuario
    nm = input("Digite o seu nome: \n")
    #é inserido na vetor nome na posição x o valor de nm
    nome.insert(x,nm)
    #a váriavel nt recebe o valor digitado pelo usuario
    nt = eval(input("Digite sua nota: \n"))
    #é inserido na vetor nota na posição x o valor de nt
    nota.insert(x,nt)
    #soma recebe o valor de soma mais nt
    soma = soma + nt
    #x recebe mais 1
    x += 1
#Se x for igual 50    
if x == 50:
    #media é igual a soma dividido por 3
    media = soma / 3
    #printa media é igual a váriavel media
    print("Media = "+str(media))
    #enquanto i for menor que 51 
    while i < 51:
        #Se nota na posição i for maior que a váriavel media  
        if nota[i] > media:
            #printa o nome na posição i
            print(nome[i])
            #a váriavel c recebe c mais 1
            c = c + 1    
        #i recebe mais 1
        i += 1
#printa o total de alunos acima da media é igual a variavel c
print("Total de alunos acima da media = "+str(c))
