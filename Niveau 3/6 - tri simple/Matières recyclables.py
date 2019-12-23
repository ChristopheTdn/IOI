nbr = int(input())
liste = []
for loop in range(nbr):
    liste.append(input())
liste.sort()
for word in liste:
    print(word)