nbr=int(input())

for loop in range(nbr):
    phrase = input()
    phrase1= list(phrase.upper().replace(' ',''))
    phrase2 = list(phrase1)
    phrase2.reverse()
    if phrase2==phrase1:
        print(phrase)


#phrase2 = phrase.reverse()
