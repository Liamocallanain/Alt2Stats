
def ss_sort(oldL):
    """ this function sorts an unsorted list and returns a copy sorted"""
    # n is the length of the list
    n=len(oldL)
    # we create an empty newList nL into which we put the items from smallest to largest
    newL=[]
    
    # we sweep across the list n times ( 1 for each new element)
    for sweep in range(n):
        # we pick out the smallest element left
        # notice that we have to look at all the list left to identify the smallest
        tiny = min(oldL)
        # we get the location of the item we want to move
        tinyLoc = oldL.index(tiny)
        # we pop it out of the old list and tag it on to the new list as the next biggest
        nL.append(oldL.pop(tinyLoc))
    # we return the sorted newList
    return newL


print(ss_sort([2,15,9,1]))

        
    
