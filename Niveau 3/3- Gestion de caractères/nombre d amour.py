def nbr_amour(prenom):
    nbr=0
    for lettre in prenom:
        nbr += ord(lettre)-65
    while nbr>=10:
        new_nbr = 0
        for lettre in str(nbr):
            new_nbr += int(lettre)
        nbr = new_nbr
    return nbr
    
prenom1,prenom2=input().split()
print ("{} {}".format(nbr_amour(prenom1),nbr_amour(prenom2)))


