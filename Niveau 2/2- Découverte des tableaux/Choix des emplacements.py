nbEmplacements = int(input())
tableau = [0]*nbEmplacements
for loop in range(nbEmplacements):
    tableau[loop] = int(input())

for marchand in range(nbEmplacements):
    print(tableau.index(marchand))

            
