import math
import fractions
#find a pattern in a set of numbers (ow)

def getdeg(numlist, cnt): #get the degree of the equation
    if allEqual(numlist):
        return (0, numlist[0]) #this thought makes me happy
    
    count = cnt #START @ 0
    templist = []
    for i in range(len(numlist) - 1): #exclude the last item (which doesn't have an item after it)
        templist.append(numlist[i+1] - numlist[i]) #append the val of index i+1 minus index i
    count += 1
    #print(templist)
    if not allEqual(templist):
        #print("Not all equal, iterating again")
        return getdeg(templist, count)
    else:
        #print(count)
        return (count, templist[0])

def allEqual(numlist):
    x = len(numlist)
    if x == 1:
        return True
    for i in range(x-1):
        if not (numlist[i] == numlist[i+1]):
            return False
    return True

def getTerms(numlist, terms, maxpower): #call with terms as []
    newtable = []
    power, fval = getdeg(numlist, 0)
    if maxpower == 0:
        maxpower = power
    terms.append(fractions.Fraction(fval, math.factorial(power)))
    if not power == 0:
        for i in range(len(numlist)):
            nval = numlist[i] - (terms[maxpower - power] * ((i + 1) ** power))
            newtable.append(nval)
        return getTerms(newtable, terms, maxpower)
    return terms

def printeq(numlist):
    #numlist = [2, 8, 9, 11, 20]
    print("Coeff\tPower")
    x = getTerms(numlist, [], 0)
    topPow = len(x) - 1
    for i in range(len(x)):
        print(str(x[i]) + "\t" + str(topPow))
        topPow -= 1

def getVals():
    x = 0
    nl = []
    try:
        while True:
            nl.append(int(input("Enter a number, or a string to find the formula describing your set: ")))
    except ValueError:
        printeq(nl)

getVals()


    
    

