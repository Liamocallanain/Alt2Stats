myList =  [6,12,6,0,6,13,6,1]

def myListMinFx(aList = []):
    listLen = len(aList)
    tempMin = aList[0]
    for i in range(listLen):
        if aList[i] < tempMin:
            tempMax = aList[i]
    return tempMin

print(myListMinFx(myList))
        