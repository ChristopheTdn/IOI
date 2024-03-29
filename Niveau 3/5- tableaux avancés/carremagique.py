def main():
    def tousNombresPresents():
        nonlocal tailleGrille
        maxVal = tailleGrille * tailleGrille + 1
        presents = [False] * maxVal
        for ligne in nombresCarre:
            for nombre in ligne:
                if (nombre <= 0) or (nombre >= maxVal) or presents[nombre]:
                    return False
                else:
                    presents[nombre] = True
        return True

    def totauxCorrects():
        nonlocal tailleGrille
        
        def totalPourDirection(linDepart, colDepart, deltaLin, deltaCol):
            nonlocal tailleGrille
            lin, col = linDepart, colDepart
            total = 0
            for loop in range(tailleGrille):
                total += nombresCarre[lin][col]
                lin += deltaLin
                col += deltaCol
            return total
        total = totalPourDirection(0, 0, 1, 1)
        if (totalPourDirection(0, tailleGrille - 1, 1, -1) != total):
            return False
        for position in range (tailleGrille):
            if totalPourDirection(position, 0, 0, 1) != total:
                return False
            if totalPourDirection(0, position, 1, 0) != total:
                return False
        return True
    
    tailleGrille = int(input())
    nombresCarre = [list(map( int, input().split() )) for loop in range(tailleGrille)]
    if tousNombresPresents() and totauxCorrects():
        print("yes")
    else:
        print("no")
        
main()