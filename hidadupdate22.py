def calculate(cost, perDown, sal, perSal, r, sar):
    currentSavings = 0
    months = 0
    while(cost * perDown > currentSavings):
        months += 1
        currentSavings += (sal * perSal/12) + (currentSavings * r/12)
        if months % 6 == 0:
            sal += sal * sar
    return months


def partA(poritonDown, r):
    sal = float(input("Enter annual salary"))
    percentSal = float(input("Enter percentage of salary as decimal"))
    cost = float(input("Enter cost"))
    return calculate(cost, poritonDown, sal, percentSal, r, 0)
#print(partA(.25, .04))

def partB(poritonDown, r):
    sal = float(input("Enter annual salary"))
    percentSal = float(input("Enter percentage of salary as decimal"))
    cost = float(input("Enter cost"))
    semiAnRaise = float(input("Enter the semi-annual raise, as a decimal"))
    return calculate(cost, poritonDown, sal, percentSal, r, semiAnRaise)


#print(partB(.25, .04))
def partC1():
    initalSal = float(input("Enter the starting salary: "))
    sar = 0.07
    r = 0.04
    down = 0.25
    cost = 1000000
    partC2(cost, down, initalSal, r, sar)

def partC2(cost, down, sal, r, sar):
    lower = 0
    upper = 10000
    extCount = 0
    while(lower < upper):
        extCount+= 1
        c = int(lower + upper) // int(2)
        months =  calculate(cost, down, sal, c/10000, r, sar)
        if months > 36:
         lower = c
        elif months < 36:
         upper = c
        if months == 36:
         print("BSR: " + str(c/10000))
         print("Steps: " + str(extCount))
         return True
    print("Impossible")
    return False
partC1()