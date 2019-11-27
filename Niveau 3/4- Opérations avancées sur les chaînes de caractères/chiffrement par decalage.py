def news_ord(lettre,cle):
    maj = False
    if not lettre.isalpha():
        return lettre
 
    if lettre >="A" and lettre <="Z":
        majuscule= True
    else:
        majuscule= False
        
    return calc_char(lettre,cle,majuscule)

def calc_char(lettre,cle,majuscule):   
     
    xchar = ord(lettre)
    decal = xchar - (cle % 26)
    
    if majuscule:
        if decal < 65:
            decal = 91 - (65-decal)
        elif decal > 90:
            decal = 64 + (decal-90)
        return chr(decal)
    else:
        if decal < 97:
            decal = 123 - (97-decal)
        elif decal > 122:
            decal = 96 + (decal-122)
        return chr(decal)


def codage(phrase,page):
    
    if page % 2 == 0:
        cle = 3 * page
    else :
        cle = -5 * page
        
    for lettre in phrase:
        print (news_ord(lettre,cle),end='')
    print()
    

'''

'''

nbpage = int(input())

for loop in range(nbpage-1):
    phrase = input()
    page = loop + 2
    codage(phrase,page)
    
