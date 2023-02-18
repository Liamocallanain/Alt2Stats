myList =  [6,12,6,0,6,13,6,1]

def myListMaxFx(aList = []):
    """ This function returns the max of a list
    parameters:
        aList: the list to be maxed
    returns:
        int:  the maximum item
    """
    # get the length of the list
    listLen = len(aList)
    # pretend that the first item ist the maximum
    tempMax = aList[0]
    # loop throught the list looking at all the items
    for i in range(listLen):
        # if the current item is bigger than the max then make it the max
        if aList[i] > tempMax:
            tempMax = aList[i]
        # otherwise do nothing and move on to next item
    # end of for loop
    
    # return the maximum item
    return tempMax

print(myListMaxFx(myList))
        