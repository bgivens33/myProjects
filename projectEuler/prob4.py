def palinTest(myPalin):
    return str(myPalin) == str(myPalin)[::-1]


highPalin = 0;


for x in range(100,1000):
    for y in range(100,1000):
        myPalin = x*y;
        if palinTest(myPalin):
            if (myPalin>highPalin):
                highPalin = myPalin
        
