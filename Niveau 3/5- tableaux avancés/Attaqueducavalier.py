def main(debug=False):
    
    def affiche(echiquier):
        for ligne in echiquier:
            for colonne in ligne:
                print (colonne,end="")
            print()

    def test_echiquier():
        echiquier = [
            ["tc.drf.t"],
            ["ppp.pppp"],
            ["...p...c"],
            [".....f.."],
            ["..C..P.."],
            ["..P.D.P."],
            ["PP.....P"],
            ["T.F.RFCT"]
        ]
        return echiquier
        
    def coord_piece(echiquier,piece):
        emplacement_piece=[]
        for ligne in range(8):
            for colonne in range(8):
                    if echiquier[ligne][colonne]==piece:
                        emplacement_piece.append("{} {}".format(str(ligne),str(colonne)))
        return emplacement_piece
    
    def coord_possible(x,y):
        if x < 0 or x > 7 or y < 0 or y > 7 :
            return False
        else:
            return True 
        
    def emplacement_possible(echiquier,emplacement_piece):
        possible_test=[]
        for i in emplacement_piece:
            x,y= map(int,i.split())

            if coord_possible(x-2,y+1):
                possible_test.append("{} {}".format(str(x-2),str(y+1)))
            if coord_possible(x-2,y-1):
                possible_test.append("{} {}".format(str(x-2),str(y-1)))
            if coord_possible(x+2,y-1):
                possible_test.append("{} {}".format(str(x+2),str(y-1)))
            if coord_possible(x+2,y+1):
                possible_test.append("{} {}".format(str(x+2),str(y+1)))
            if coord_possible(x+1,y-2):
                possible_test.append("{} {}".format(str(x+1),str(y-2)))
            if coord_possible(x-1,y-2):     
                possible_test.append("{} {}".format(str(x-1),str(y-2)))
            if coord_possible(x+1,y+2):
                possible_test.append("{} {}".format(str(x+1),str(y+2)))
            if coord_possible(x-1,y+2):  
                possible_test.append("{} {}".format(str(x-1),str(y+2)))

        return possible_test

    def prise_possible(echiquier,deplacements):
        for deplacement in deplacements:
            x,y = map(int,deplacement.split())
            if echiquier[x][y].islower():
                return "yes"
        return 'no'


    debug = False
    tailleGrille = 8
    if debug :
        entree=list(test_echiquier())
    else:
        entree = [list(input().split()) for loop in range(tailleGrille)]
    echiquier=[]
    for i in entree:
        for j in i:
            echiquier.append(list(j))
    
    print(prise_possible(echiquier,emplacement_possible(echiquier,coord_piece(echiquier,"C"))))

debug=False
main(debug)
