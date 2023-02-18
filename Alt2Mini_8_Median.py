myList =  [6,12,6,0,7,13,7,1]
print("myList = ", myList)


def myListMedianFx(aList = []):
    aList.sort()
    print(aList)
    myListLen= len(aList)
    if myListLen % 2 == 1:
      print ("The list has an odd number of terms")
      medianPos = (myListLen +1)//2 -1
      print ("The median is at 0-index", medianPos)
      myMedian = (aList[medianPos])
      print("The median is ", myMedian)
    else:
        print ("The list has an even number of terms")
        medianPos1 = (myListLen +1)//2 -1
        medianPos2 = (myListLen +1)//2 
        print ("The median is at 0-indexes", medianPos1,medianPos2)
        myMedian = (aList[medianPos1]+aList[medianPos2])/2
        print("The median is ", myMedian)
    return(myMedian)
        
print ("The median is ", myListMedianFx(myList))
            
        

