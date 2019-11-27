def main ():
    def init(debug):
        plateau=[]
        if False :
            tailleGrille=12
            entree=list(def_plateau())
            
        else:
            tailleGrille = int(input())
            entree=[]
            for i in range(tailleGrille):
                entree.append([input()])
            
        for i in entree:    
            j = i[0].split(" ")
            plateau.append([int(x) for x in j])
            
        return plateau
    
    def affiche(plateau):
        for ligne in plateau:
            for colonne in ligne:
                print (colonne,end="")
            print()

    def def_plateau():
        plateau = [
            ["0 0 2 0 1 0"],
            ["0 1 2 2 2 1"],
            ["0 0 2 0 1 0"],
            ["0 0 2 1 0 0"],
            ["0 0 1 0 0 0"],
            ["0 1 0 0 0 0"]
        ]
        return plateau
    def renvois_valeur(plateau,x,y):
        if x<0 or x > len(plateau[0])-1 or y<0 or y > len(plateau[0])-1:
            return 0
        else:
            return plateau[x][y]
        
    def test_case(plateau,x,y):
        # horizontal
        valide1 = True
        valide2 = True
        valide3 = True
        valide4 = True
        valide5 = True
        valide6 = True
        valide7 = True
        valide8 = True
        resultat = renvois_valeur(plateau,x,y)
        for i in range(5):
            if renvois_valeur(plateau,x+i,y) != resultat and valide1:
                valide1 = False
            if renvois_valeur(plateau,x-i,y) != resultat and valide2:
                valide2= False
            if renvois_valeur(plateau,x,y+i) != resultat and valide3:
                valide3 = False
            if renvois_valeur(plateau,x,y-i) != resultat and valide4:
                valide4= False
            if renvois_valeur(plateau,x+i,y+i) != resultat and valide5:
                valide5 = False
            if renvois_valeur(plateau,x-i,y+i) != resultat and valide6:
                valide6 = False
            if renvois_valeur(plateau,x+i,y-i) != resultat and valide7:
                valide7 = False
            if renvois_valeur(plateau,x-i,y-i) != resultat and valide8:
                valide8 = False
        if valide1 or valide2 or valide3 or valide4 or valide5 or valide6 or valide7 or valide8:
            return resultat
        else:
            return 0             
    def test_plateau(plateau):
        
        largeur=len(plateau[0])
        for x in range(largeur) : 
            for y in range(largeur):
                resultat = test_case(plateau,x,y)
                if resultat>0:
                    return resultat
        return 0
                
    plateau = init(False)
    print(test_plateau(plateau))
    
if __name__ == "__main__":
    main()