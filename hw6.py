#
# 20fa-cs115bc
#
# Antonio R. Nicolosi 
# 20201120
#************************************************************
# *  Name  : Adam Woo
# * Pledge : I pledge my honor that I have abided by the Stevens Honor System.
#************************************************************

# Programming problems with one-dimensional arrays.
def isWithinRange(arr, min, sup):
    """
     Return True if and only if all entries in the array fall between
     the specified values, with min being permitted but sup being just
     beyond the allowable range).
     
     Sample input/outputs:
     Let arr = [3, -5,  7, -1, -8, 0, -6, -2]
     Then:
	 * isWithinRange(arr, -6, 10) -> False;
	 * isWithinRange(arr, -8, 10) -> True;
	 * isWithinRange(arr, -8, 7)  -> False;
	 */
    """
    count=0
    for x in arr:
        if x>=min and x<sup:
            count+=1
    return count == len(arr)
            


def isPermutation(arr):
    """Returns True if and only if its entries, taken as a set, consist
    of all the numbers between 0 and len(arr)-1 (possibly permuted
    according to some arbitrary order).

    Sample input/outputs:
    * isPermutation([3, -5, 7, 4, -1, -8, 0, -6, -2]) --> False
    * isPermutation([3, 5, 7, 4, 1, 8, 0, 6, 2])      --> True
    * isPermutation([3, 1, 0, 3, 0])                  --> False
    * isPermutation([])                               --> True
    """
    count=0
    for x in range(len(arr)):
        if x in arr:
            count+=1
    return count==len(arr)

        
    

def isCyclic(arr):
    """
    Return true if-and-only-if the sequence arr[0], * arr[arr[0]],
    arr[arr[arr[0]]], ... reaches 0 * after traversing all entries in
    arr.

    Sample input/outputs:
    * isCyclic([3, 5, 7, 4, 1, 8, 0, 6, 2)] --> True
    * isCyclic([3, 5, 7, 4, 1, 8, 6, 0, 2]) --> False
    * isCyclic([3, 1, 0, 3, 0])             --> False
    * isCyclic([])                          --> True
    """
    if arr == []:
        return True
    else:
        nextN = arr[0]
        count = 0
        while True:
            pastN = nextN
            nextN = arr[nextN]
            count += 1
            if count == len(arr) and pastN == 0:
                return True
            if count>=len(arr):
                break
        return False

            

def isSloppilySorted(arr, k):
    """
    Return True if-and-only-if the entries in arr are sorted sloppily 
    "up to k", that is, every entry precedes at most k smaller values
     and follows at most k larger values.

    Sample input/outputs:
    * isSloppilySorted([3, 2, 1, 0, 4, 8, 7, 6, 5], 3) --> True
    * isSloppilySorted([3, 2, 1, 0, 4, 8, 7, 6, 5], 2) --> False
    * isSloppilySorted([0, 1, 2, 3, 4, 5, 6, 7, 8], 1) --> True
    * isSloppilySorted([], 3)                          --> True
    """
    if arr == []:
        return True
    if k==0:
        return arr==sorted(arr)
    for x in range(len(arr)):
        if x == len(arr)-1:
            return True
        if arr[x+1]<arr[x]:
            if x+k+1 >= len(arr):
                return True
            for y in range(k):
                if arr[x+y+1]>arr[x]:
                    break
                elif y+1==k and arr[x+y+2]<arr[x]:
                    return False
    return False
                    
        







        
