debug = False
if not debug:
    Qtstock, Qtarrivee = map(int, input().split())
    stock = list(map(int, input().split()))
    arrivee = list(map(int, input().split()))
else:
    Qtstock, Qtarrivee = 5, 4
    stock = []
    arrivee = [3, 2, 3, 1, 3]

for i in arrivee:
    cherche = True
    while cherche:
        if len(stock) == 0:
            print(0, end=" ")
            stock.append(i)
            cherche = False
            break
        if stock[-1] < i:
            print(len(stock), end=" ")
            stock.append(i)
            cherche = False
        else:
            for index in range(len(stock)):
                if stock[index] >= i:
                    stock.insert(index, i)
                    print(index, end=" ")
                    cherche = False
                    break
print()
for i in stock:
    print(i, end=" ")

