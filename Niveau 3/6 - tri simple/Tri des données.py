input()
course = list(map(int,input().split()))
course.sort()
for i in course:
    print(i,end=" ")