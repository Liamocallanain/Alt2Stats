myList =  [6,12,6,0,6,13,6,1]

def myListCounterLFx(aList = []):
    
    
    counterList =[]
    lenList = len(aList)
    
    for i in range(lenList):
        counterList.append(0)
        counterList[i] = aList.count(aList[i])
    
    return counterList
        

print("myList is ", myList)
print("counterList is", myListCounterLFx(myList))
