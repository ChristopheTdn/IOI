stock, camion = map(int, input().split())
tableau = list(map(int, input().split()))
for i in range(camion):
    s = max(tableau)
    tableau.remove(s)
    print(s, " ", end="")
