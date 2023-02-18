import Alt2Mini_Min
import Alt2Mini_Max

myList =  [6,12,6,0,6,13,6,1]

def myListRangeFx(aList = []):
    tempMax = Alt2Mini_Max.myListMaxFx(aList)
    tempMin = Alt2Mini_Min.myListMinFx(aList)
    tempRange = tempMax  - tempMin
    return tempRange

print(myListRangeFx(myList))
