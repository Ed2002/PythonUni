#a váriavel nomecarro recebe o valor digitado pelo usuario
nomecarro = input("Insira o nome do carro: \n")
#a váriavel prefabric recebe o valor digitado pelo usuario
prefabric = eval(input("Digite o preço de fabrica: \n"))
#a váriavel soma recebe prefabric multiplicado por 0.28
soma = prefabric * 0.28
#a váriavel soma2 recebe prefabric multiplicado por 0.45
soma2 = prefabric * 0.45
#a váriavel precoc é igual a soma mais soma2 mais prefabric
precoc = soma+soma2+prefabric
#printa o nome do carro o preço de mercado o custo de distribuição e o valor do imposto
print("\nO carro "+nomecarro+" custara "+str(precoc)+"\n com o custo de "+str(soma)+" do distribuidor\ne tambem "+str(soma2)+" de imposto")