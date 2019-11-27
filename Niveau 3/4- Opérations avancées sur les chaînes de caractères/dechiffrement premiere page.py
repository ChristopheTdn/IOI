cle = input()
message=input()
for lettre in message:
    maj = False
    if lettre.isalpha():
        if lettre >="A" and lettre <="Z":
            maj = True
        if maj:
            print(cle[ord(lettre)-65].upper(),end="")
        else:
            print(cle[ord(lettre)-97],end="")
    else:
        print(lettre,end="")