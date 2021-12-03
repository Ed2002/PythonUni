altura = []
x = 0
while x < 21:
    dado = input("Digite")
    altura.insert(x,dado)
    x += 1
    if x == 20:
        for i in altura:
            print(i)


