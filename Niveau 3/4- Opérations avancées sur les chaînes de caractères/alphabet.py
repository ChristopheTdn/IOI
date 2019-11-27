test = "aeiouy"
for ascii in range(ord('a'), ord('z') + 1):
    car= chr(ascii)
    if car in test:
        print(car+" ",end ='')