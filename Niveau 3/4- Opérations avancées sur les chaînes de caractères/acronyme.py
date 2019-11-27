acronyme= input()
nblivre= int(input())
for loop in range(nblivre):
    name=input().upper()
    namesplit=name.split()
    acronew=""
    nicetitle=""
    for word in namesplit:
        acronew+= word[0]
        nicetitle += word[0] + word[1:].lower()+" "
    if acronew == acronyme:
        print(nicetitle)