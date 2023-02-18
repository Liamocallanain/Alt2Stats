myList =  [6,12,6,0,6,13,6,1]


def myListTotalFx(aList = []):
    """ This function returns the total of a list
    parameters:
        aList: the list to be totalled
    returns:
        int: the total of the list
    """
    # see how long the list is
    listLen = len(aList)
    # initialize the temporary total to zero
    tempTotal = 0
    # loop through the list from 0 to listLen-1
    for i in range(listLen):
        # add that list item to the total
        tempTotal = tempTotal + aList[i]
    #end of for loop
        
    # when the loop is finished return the total ( an integer or float)
    return tempTotal

print("The total is ", myListTotalFx(myList))
        