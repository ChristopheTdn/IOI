deplacement = int(input())
tableau=[]
for loop in range(deplacement):
    move = int(input())
    if move == 1: 
        tableau.append(2)
    elif move == 2:
        tableau.append(1)
    elif move == 3:
        tableau.append(3)
    elif move == 4:
        tableau.append(5)
    elif move == 5:
        tableau.append(4)
tableau.reverse()
for d in tableau:
    print(d)