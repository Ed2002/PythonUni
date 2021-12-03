#váriavel hr_inc recebe o valor de digitado pelo o usuario
hr_inc = eval(input("Digite a hora de inicio: \n"))
#váriavel hr_fim recebe o valor de digitado pelo o usuario
hr_fim = eval(input("Digite a hora de termino: \n"))
#Se hr_inc for maior que hr_fim
if hr_inc >= hr_fim:
    #duração recebe o valor de 24 - hr_inc + hr_fim
    duracao = (24 - hr_inc) + hr_fim
    #printa a váriavel duração
    print("Duração = "+str(duracao))
#Se não
else: 
    #duração recebe hr_inc - hr_fim
    duracao = hr_fim - hr_inc
    #printa a váriavel duração
    print("Duração = "+str(duracao))