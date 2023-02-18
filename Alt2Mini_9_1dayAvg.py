myList = [6,12,6,0,6,13,6,1]
dayAvgL = []

def dayAvg(aList):
    lenDay = 4
    for k in range (len(aList)//4):
        thisDayTotal=0
        for j in range (k*4,(k+1)*4,1):
            thisDayTotal= thisDayTotal+myList[j]
        thisDayAvg=thisDayTotal/lenDay
        dayAvgL.append(thisDayAvg)
    return dayAvgL

print(dayAvg(myList))
        
        