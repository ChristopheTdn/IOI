phrase = input()
statistic = [0]*27
print(phrase)
for lettre in phrase:
    lettre=lettre.upper()
    if lettre >="A" and lettre <="Z":
        statistic[0]+=1
        statistic[ord(lettre)-64] += 1
for loop in range(27):
     if loop>0:
        print(round(statistic[loop]/statistic[0],6))