#Adam Woo
#I pledge my honor that I have abided by the Stevens Honor System.

def dotProduct(L,K):
    if L[:] == [] or K[:]==[]:
        return 0
    else:
        return (L[0]*K[0])+dotProduct(L[1:],K[1:])
#takes first and multiplies
#then calls itself without those numbers and adds together
    
    
def expand(S):
    if S=="":
        return []
    else:
        return [S[0]]+(expand(S[1:]))
#takes first letter as list then adds to list
#calling on itself without that first letter, taking the second letter in turn.


def deepMember(e,L):
    if isinstance(L[0], list):
        if deepMember(e,L[0]):
            return True
    
    if e == L[0]:
        return True
    elif L[1:] != []:
        return deepMember(e,L[1:])
    else:
        return False
#checks if value is list
#if its equal return true
#if not, remove it and try next
#if its empty return false


    
def removeAll(e,L):
    if L == []:
        return []
    if L[0]!= e:
        return [L[0]] + removeAll(e,L[1:])
    else:
        return removeAll(e,L[1:])
#if it is there remove it
#keep calling to see if its there
#eventually wont be there, so it wont be called again and itll return the L without e


def myFilter(f, L):
    if L == []:
        return []
    elif f(L[0]):
        return [L[0]] + myFilter(f,L[1:])
    else:
        return [] + myFilter(f,L[1:])
#if first value true it adds to a list if not it moves on to next without adding to list
#if empty it returns nothing


def deepReverse(L):
    if L!=[] and isinstance(L[-1], list):
        return [deepReverse(L[-1])] + deepReverse(L[:-1])
    if L ==[]:
        return []
    return [L[-1]] + deepReverse(L[:-1])
#takes last and puts it in front
#removes last and puts it next
#if its a list it will reverse that list and continue with the rest



    
