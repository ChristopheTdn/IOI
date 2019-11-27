nbNoms = int(input())
for loop in range(nbNoms):
    password = input()
    validate = True
    if password[0].isdecimal():
        validate = False
    for caractere in password:
        if not (("0" <= caractere and caractere <= "9") or ("a" <= caractere and caractere <= "z") or ("A" <= caractere and caractere <= "Z") or (caractere == "_"))  :
            validate = False
    if validate :
        print ("YES")
    else:
        print("NO")