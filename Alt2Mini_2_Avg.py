myList =  [6,12,6,0,6,13,6,1]

import Alt2Mini_1_Total

def myListAvgFx(aList = []):
    tempTotal = Alt2Mini_1_Total.myListTotalFx(aList)
    
    tempAvg = tempTotal/len(aList)
    return tempAvg

print("The average is ", myListAvgFx(myList))
        