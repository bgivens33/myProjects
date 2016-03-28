def isPrime(n):
    check = True
    if n<=2:
        check = False
    else:
        for i in range(2,n):
            if n%i ==0:
                check = False
    return check

myNum = 10001

primeList = []

i = 2
while len(primeList)<myNum:
    if isPrime(i):
        primeList.append(i)
        i+=1
    else:
        i+=1
print(primeList[-1])
    
