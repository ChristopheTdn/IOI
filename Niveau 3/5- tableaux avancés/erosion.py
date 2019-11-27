image =[]
def main ():
    def init(debug):
        global image
        if debug :
            facteur = 2
            hauteur,largeur  = 12,16
            photo = def_image()
            for loop in range(hauteur):
                image.append(list(photo[loop][0]))
        else:
            facteur = int(input())
            hauteur,largeur  = map(int,input().split())
            image = [list(input()) for loop in range(hauteur)]
           
        return hauteur,largeur,facteur
    
    
    
    
    def affiche():
        global image
        for ligne in image:
            for colonne in ligne:
                print (colonne,end="")
            print()

    def def_image():
        plateau = [
            ["...########....."],
            ["..#########....."],
            [".##########....."],
            ["################"],
            ["################"],
            ["######..#######."],
            [".######.#######."],
            ["..############.."],
            ["...###########.."],
            ["....#########..."],
            ["......#######..."],
            ["........####...."]
        ]
        return plateau
    
    def renvois_valeur(y,x,largeur,hauteur):
        global image
        test = [(0,1),(0,-1),(1,0),(-1,0)]
        teinte =0
        for v1,v2 in test:
            if  not (x+v2<0 or x+v2 >= largeur or y+v1<0 or y+v1 >= hauteur):
                if image[y+v1][x+v2] == "#" :
                    teinte +=1
        if teinte < 4 :
            return "."
        else:
            return "#"
        
    def erosion_core(largeur,hauteur,facteur):
        global image
        import copy
        test = [(0,1),(0,-1),(1,0),(-1,0)]
        image_tampon = copy.deepcopy(image)
        for loop in range(facteur):
            for x in range(largeur):
                for y in range(hauteur):
                    car = image[y][x]
                    if car == '#':
                        image_tampon[y][x] = renvois_valeur(y,x,largeur,hauteur)
            image = copy.deepcopy(image_tampon)
        return image

    global image            
    hauteur,largeur,facteur = init(False)
    erosion_core(largeur,hauteur,facteur)
    affiche()
    
if __name__ == "__main__":
    main()