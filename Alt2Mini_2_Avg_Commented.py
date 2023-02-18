myList =  [6,12,6,0,6,13,6,1]

# we need the list total module 
import Alt2Mini_1_Total

def myListAvgFx(aList = []):
    """ This function returns the average of a list
    parameters:
        aList: the list to be averaged
    returns:
        float: the average of the list
    """
    # we first add up all the list items using a Fx
    tempTotal = Alt2Mini_1_Total.myListTotalFx(aList)
    # we divide the total by the number of items
    tempAvg = tempTotal/len(aList)
    # we return the average which may contain decimals
    return tempAvg

print("The average is ", myListAvgFx(myList))
        