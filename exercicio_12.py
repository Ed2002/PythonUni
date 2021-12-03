#a váriavel rsl é igual a um vetor
rsl = []
#a váriavel rnt é igual a um vetor
rnt = []
#a váriavel rsd é igual a um vetor
rsd = []
#a váriavel rco é igual a um vetor
rco = []
#a váriavel rnd é igual a um vetor
rnd = []
#a váriavel x é igual a 0
x = 0
#enquanto x for menor que 5
while x < 5:
    #a váriavel vrsl recebe o valor digitado pelo usuario
    vrsl = eval(input("Digite os votos da região 1 do candidato "+str(x+1)+":\n"))
    #é inserido no vetor rsl na posição x e o valor da váriavel vrsl
    rsl.insert(x,vrsl)
    #a váriavel vrnt recebe o valor digitado pelo usuario
    vrnt = eval(input("Digite os votos da região 2 do candidato "+str(x+1)+":\n"))
    #é inserido no vetor rnt na posição x e o valor da váriavel vrnt
    rnt.insert(x,vrnt)
    #a váriavel vrsd recebe o valor digitado pelo usuario
    vrsd = eval(input("Digite os votos da região 3 do candidato "+str(x+1)+":\n"))
    #é inserido no vetor rsd na posição x e o valor da váriavel vrsd
    rsd.insert(x,vrsd)
    #a váriavel vrco recebe o valor digitado pelo usuario
    vrco = eval(input("Digite os votos da região 4 do candidato "+str(x+1)+":\n"))
    #é inserido no vetor rco na posição x e o valor da váriavel vrco
    rco.insert(x,vrco)
    #a váriavel vrnd recebe o valor digitado pelo usuario
    vrnd = eval(input("Digite os votos da região 5 do candidato "+str(x+1)+":\n"))
    #é inserido no vetor rnd na posição x e o valor da váriavel vrnd
    rnd.insert(x,vrnd)
    #x recebe mais 1
    x += 1
#a váriavel c1 recebe rsl na posição 0 mais rsd na posição 0 mais rnd na posição 0 mais rnt na posição 0 mais rco na posição 0
c1 = (rsl[0] + rsd[0] + rnd[0] + rnt[0] + rco[0])
#a váriavel c1 recebe rsl na posição 1 mais rsd na posição 1 mais rnd na posição 1 mais rnt na posição 1 mais rco na posição 1
c2 = (rsl[1] + rsd[1] + rnd[1] + rnt[1] + rco[1])
#a váriavel c1 recebe rsl na posição 2 mais rsd na posição 2 mais rnd na posição 2 mais rnt na posição 2 mais rco na posição 2
c3 = (rsl[2] + rsd[2] + rnd[2] + rnt[2] + rco[2])
#a váriavel c1 recebe rsl na posição 3 mais rsd na posição 3 mais rnd na posição 3 mais rnt na posição 3 mais rco na posição 3
c4 = (rsl[3] + rsd[3] + rnd[3] + rnt[3] + rco[3])
#a váriavel c1 recebe rsl na posição 4 mais rsd na posição 4 mais rnd na posição 4 mais rnt na posição 4 mais rco na posição 4
c5 = (rsl[4] + rsd[4] + rnd[4] + rnt[4] + rco[4])
#printa Região Sul
print("\n***Região Sul***")
#printa os votos do candidato 1 na região sul
print("\nCandidato 1 = "+str(rsl[0]))
#printa os votos do candidato 2 na região sul
print("\nCandidato 2 = "+str(rsl[1]))
#printa os votos do candidato 3 na região sul
print("\nCandidato 3 = "+str(rsl[2]))
#printa os votos do candidato 4 na região sul
print("\nCandidato 4 = "+str(rsl[3]))
#printa os votos do candidato 5 na região sul
print("\nCandidato 5 = "+str(rsl[4]))
#printa Região Sudeste
print("\n***Região Sudeste***")
#printa os votos do candidato 1 na região sudeste
print("\nCandidato 1 = "+str(rsd[0]))
#printa os votos do candidato 2 na região sudeste
print("\nCandidato 2 = "+str(rsd[1]))
#printa os votos do candidato 3 na região sudeste
print("\nCandidato 3 = "+str(rsd[2]))
#printa os votos do candidato 4 na região sudeste
print("\nCandidato 4 = "+str(rsd[3]))
#printa os votos do candidato 5 na região sudeste
print("\nCandidato 5 = "+str(rsd[4]))
#printa Região Centro-Oeste
print("\n***Região Centro-Oeste***")
#printa os votos do candidato 1 na região centro-oeste
print("\nCandidato 1 = "+str(rco[0]))
#printa os votos do candidato 2 na região centro-oeste
print("\nCandidato 2 = "+str(rco[1]))
#printa os votos do candidato 3 na região centro-oeste
print("\nCandidato 3 = "+str(rco[2]))
#printa os votos do candidato 4 na região centro-oeste
print("\nCandidato 4 = "+str(rco[3]))
#printa os votos do candidato 5 na região centro-oeste
print("\nCandidato 5 = "+str(rco[4]))
#printa Região Norte
print("\n***Região Norte***")
#printa os votos do candidato 1 na região norte
print("\nCandidato 1 = "+str(rnt[0]))
#printa os votos do candidato 2 na região norte
print("\nCandidato 2 = "+str(rnt[1]))
#printa os votos do candidato 3 na região norte
print("\nCandidato 3 = "+str(rnt[2]))
#printa os votos do candidato 4 na região norte
print("\nCandidato 4 = "+str(rnt[3]))
#printa os votos do candidato 5 na região norte
print("\nCandidato 5 = "+str(rnt[4]))
#printa Região Nordeste
print("\n***Região Nordeste***")
#printa os votos do candidato 1 na região nordeste
print("\nCandidato 1 = "+str(rnd[0]))
#printa os votos do candidato 2 na região nordeste
print("\nCandidato 2 = "+str(rnd[1]))
#printa os votos do candidato 3 na região nordeste
print("\nCandidato 3 = "+str(rnd[2]))
#printa os votos do candidato 4 na região nordeste
print("\nCandidato 4 = "+str(rnd[3]))
#printa os votos do candidato 5 na região nordeste
print("\nCandidato 5 = "+str(rnd[4]))
#printa votos totais
print("\n***Votos totais***")
#printa o total de votos do candidato 1
print("\nCandidato 1 = "+str(c1))
#printa o total de votos do candidato 2
print("\nCandidato 2 = "+str(c2))
#printa o total de votos do candidato 3
print("\nCandidato 3 = "+str(c3))
#printa o total de votos do candidato 4
print("\nCandidato 4 = "+str(c4))
#printa o total de votos do candidato 5
print("\nCandidato 5 = "+str(c5))
#Se c1 for maior que c2 e c1 for maior que c3 e c1 for maior que c4 e c1 for maior que c5  
if c1 > c2 and c1 > c3 and c1 > c4 and c1 > c5:
    #a váriavel g recebe Candidato 1
    g = "Candidato 1"
#Se c2 for maior que c3 e c2 for maior que c4 e c2 for maior que c1 e c2 for maior que c5
elif c2 > c3 and c2 > c4 and c2 > c1 and c2 > c5:
    #a váriavel g recebe Candidato 2  
    g = "Candidato 2"
#Se c3 for maior que c1 e c3 for maior que c2 e c3 for maior que c4 e c3 for maior que c5
elif c3 > c1 and c3 > c2 and c3 > c4 and c3 > c5:
    #a váriavel g recebe Candidato 3
    g = "Candidato 3"
#Se c4 for maior que c1 e c4 for maior que c2 e c4 for maior que c3 e c4 for maior que c5
elif c4 > c1 and c4 > c2 and c4 > c3 and c4 > c5:
    #a váriavel g recebe Candidato 4
    g = "Candidato 4"
#Se c5 for maior que c1 e c5 for maior que c2 e c5 for maior que c3 e c5 for maior que c4
elif c5 > c1 and c5 > c2 and c5 > c3 and c5 > c4:
    #a váriavel g recebe Candidato 5
    g = "Candidato 5"
#printa Vencedor da Eleição
print("\n*****Vencedor da Eleição*****\n")
#printa o vencedor da eleição é igual a váriavel g
print("O vencedor da eleição é: "+g)