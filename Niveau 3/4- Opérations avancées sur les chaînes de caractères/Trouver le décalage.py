def renvois_codage(phrase):
    phrase = phrase.upper()
    tableau = [0]*27
    for lettre in phrase:
        if lettre >="A" and lettre <="Z":
            tableau[ord(lettre)-64] += 1
    cle = tableau.index(max(tableau))-5
    return cle
    
    



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
    decal = xchar - cle 
    
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

def codage2 (phrase, cle):
    for lettre in phrase:
        print (news_ord(lettre,cle),end='')
    print()    
    
    
    
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

phrase = input ()
codage2(phrase,(renvois_codage(phrase)))