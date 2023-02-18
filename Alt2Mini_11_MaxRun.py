myList = [6, 12, 6, 0, 6, 13, 6, 1]

def getMaxRun(aList):

    tempMaxL =[]
    maxRunCount =[]
    tempMax = 0
      
    for i in range (len(myList)):
        print(myList[i],end =" ")
        if myList[i]>tempMax:
            tempMax = myList[i]
        tempMaxL.append(tempMax)
    print("\n")  
    return tempMaxL
  
print(getMaxRun(myList))

    

