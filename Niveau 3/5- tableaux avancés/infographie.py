def creatableau(ligne,colonne,carac="."):
    tableau=[]
    for j in range(ligne):
        coltab = ["."]*colonne
        tableau.append(coltab)    
    return tableau

def dessine_rectangle(x,y,x2,y2,car,tableau):
    for i in range(y2-y+1):
        for j in range(x2-x+1):
            tableau[j+x][i+y]=car
    return tableau

def affiche(tableau):
    for i in tableau:
        for z in i:
            print (z,end="")
        print()
    
    
    
nbligne,nbcolonne  = map(int,input().split())
nbrectangle = int(input())

tableau= creatableau(int(nbligne),int(nbcolonne))

for i in range(nbrectangle):
    x,y,x2,y2,car = input().split()
    tableau = dessine_rectangle(int(x),int(y),int(x2),int(y2),car,tableau)

affiche(tableau)
