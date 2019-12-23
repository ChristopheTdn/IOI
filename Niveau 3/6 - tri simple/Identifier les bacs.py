nbBacs = int(input())
depot = {}
for loop in range(nbBacs):
    idBac, niveau = map(int, input().split())
    depot[idBac] = niveau

s = sorted(depot.items(), key=lambda t: t[0])

for loop in sorted(s, key=lambda t: t[1]):
    print("{} {}".format(loop[0], loop[1]))
