myList =  [6,12,6,0,6,13,6,1]
print("myList = ",myList)

import Alt2Mini_6_CounterL

def myListModeFx(aList = []):
    counterList = Alt2Mini_6_CounterL.myListCounterLFx(aList)
    print("counterList=",counterList)
    maxIndex = counterList.index(max(counterList))
    myMode=aList[maxIndex]
    return myMode

print("myMode is", myListModeFx(myList))
    
