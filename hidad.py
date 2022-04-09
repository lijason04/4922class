def partA(poritonDown, r):
    currentSavings = 0
    sal = float(input("Enter annual salary"))
    percentSal = float(input("Enter percentage of salary as decimal"))
    cost = float(input("Enter cost"))
    counter = 0
    while(currentSavings < cost * poritonDown):

        currentSavings += (sal *  percentSal/12) + (currentSavings * r/12)
        counter+= 1
    return counter
#print(partA(.25, .04))

def partB(poritonDown, r):
    currentSavings = 0
    sal = float(input("Enter annual salary"))
    percentSal = float(input("Enter percentage of salary as decimal"))
    cost = float(input("Enter cost"))
    semiAnRaise = float(input("Enter the semi-annual raise, as a decimal"))
    counter = 0
    while(currentSavings < cost * poritonDown):
        counter+= 1

        currentSavings += (sal *  percentSal/12) + (currentSavings * r/12)
        if (counter % 6 == 0):
                sal += sal * semiAnRaise
    return counter

#print(partB(.25, .04))

def partC():
    initalSal = float(input("Enter the starting salary: "))
    sar = 0.07
    anret = 0.04
    down = 0.25
    cost = 1000000
    a = 0
    b = 10000
    extCount = 0
    currentSavings = 0
    counter = 0
    while(a < b):
        currentSavings = 0
        copiedSal = initalSal
        extCount+= 1
        c = int(a+b) // int(2)
        counter = 0
        while(currentSavings < cost * down):
            counter+= 1
            currentSavings += (copiedSal *  (c/10000)/12) + (currentSavings * anret/12)
            if (counter % 6 == 0):
               copiedSal += copiedSal * sar
        if counter > 36:
         a = c
        elif counter < 36:
         b = c
        if counter == 36:
         print("BSR: " + str(c/10000))
         print("Steps: " + str(extCount))
         return True
    print("Impossible")
    return False
partC()