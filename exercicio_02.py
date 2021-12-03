#pega o valor informado pelo usuario e armazena na váriavel dp
dp = eval(input("Informe a distância percorrida: "))
#pega o valor informado pelo usuario e armazena na váriavel tg
tg = eval(input("Informe o tempo gasto: "))
#vm recebe a divisão de dp por tg
vm = dp/tg
#qcg recebe a divisão de dp por 12
qcg = dp/12
#printa o valor da váriavel vm
print("Velocidade media = "+str(vm))
#printa o valor da váriavel qcg
print("Quantidade de combustível gasto = "+str(qcg))