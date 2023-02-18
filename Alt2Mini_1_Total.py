myList =  [6,12,6,0,6,13,6,1]


def myListTotalFx(aList = []):
    listLen = len(aList)
    tempTotal = 0
    for i in range(listLen):
        tempTotal = tempTotal + aList[i]
    return tempTotal

print("The total is ", myListTotalFx(myList))
        