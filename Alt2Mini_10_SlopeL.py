myList =  [6,12,6,0,6,13,6,1]

def myListSlopeLFx(aList = []):
    
    
    slopeList =[]
    lenList = len(aList)
    
    for i in range(lenList-1):
        slopeList.append(0)
        tempSlope = aList[i+1] - aList[i]
        slopeList[i] = tempSlope
        
    
    return slopeList
        

#print("myList is         ",myList)
#print("myList slopes are ",myListSlopeLFx(myList))
