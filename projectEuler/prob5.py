i = 19501100

while True:
    for j in range(1,21):
        if i % j != 0:
            break
    if j == 20:
        print(i)
        break
    i+=20
    
    
