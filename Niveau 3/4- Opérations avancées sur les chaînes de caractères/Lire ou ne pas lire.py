nbr=int(input())
livre= [""]*nbr
for loop in range(nbr):
    livre[loop]=input()
alpha=chr(ord("A")-1)
for loop in range(nbr):
    if livre[loop] > alpha:
        print (livre[loop])
        alpha = livre[loop]