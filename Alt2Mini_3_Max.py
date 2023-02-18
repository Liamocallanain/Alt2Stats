myList =  [6,12,6,0,6,13,6,1]

def myListMaxFx(aList = []):
    listLen = len(aList)
    tempMax = aList[0]
    for i in range(listLen):
        if aList[i] > tempMax:
            tempMax = aList[i]
    return tempMax

print("The maximum is", myListMaxFx(myList))
        