nbr= int(input())
newtab=[""]*nbr
for i in range(nbr):
    titre1,titre2 = input().split()
    newtab[i]="{} {}".format(titre2,titre1)
newtab.sort()
for i in range(nbr):
    print(newtab[i])
