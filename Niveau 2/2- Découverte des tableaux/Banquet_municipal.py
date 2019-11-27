nbr_Tab = int(input())
table=[]
chang_pos = int(input())

for loop in range(nbr_Tab):
    table.append(int(input()))



for loop in range(chang_pos):
    pos1 = int(input())
    pos2 = int(input())
    table[pos1],table[pos2]=table[pos2],table[pos1]

for loop in range(nbr_Tab):
    print (table[loop])
