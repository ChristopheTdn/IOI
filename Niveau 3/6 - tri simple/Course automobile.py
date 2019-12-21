nbAutomobiles = int(input())
course = list(map(int,input().split()))
coursePasTerminee = True
course.insert(0,0)
etape=[]
for i in range(nbAutomobiles+1):
    etape.append(i)
tour=0
deroulement=[]
voiture = nbAutomobiles

while coursePasTerminee:
    while course.index(voiture) != etape.index(voiture):
        placeVoiture = etape.index(voiture)
        deroulement.append([etape[placeVoiture],etape[placeVoiture-1]]) 
        tour += 1
        etape[placeVoiture],etape[placeVoiture-1] =   etape[placeVoiture-1],etape[placeVoiture]
    voiture -= 1
    if etape == course :
        coursePasTerminee = False

print (tour)
deroulement.reverse()
for i in deroulement:
    print("{} {}".format(i[0],i[1]))
    