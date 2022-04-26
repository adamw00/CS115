####################################################################################
# Name: Adam Woo
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
####################################################################################


# The binary format you'll be working with for this assignment is called R2L,
# as it is a right-to-left representation.
####################################################################################
## Ex: 8 in decimal is 1000 in standard binary (2^3),
## and represented as a list [0, 0, 0, 1] in our R2L representation.
####################################################################################

# Notice that this makes it very easy to work with binary,
# by using num[0] to grab the least significant bit (2^0)!
#
# Please fill out the following 4 functions below using recursion, as specified.

# Given an integer x >= 0, convert it to the R2L binary format.
# Take note that both [] and [0] are used to represent 0 in R2L
def decimalToBinary(x):
    if x == 0: 
        return []
    else:
        return [x % 2] + decimalToBinary(int(x // 2))
    #sees if the output is divisible by 2 if it isnt, a 1 is added
    #if it is, a 0 is added and it decrements by 1/2.

# Given an R2L formatted number, return the integer it is equivalent to.
# The function should function with both [] and [0] returning 0.
def binaryToDecimal(num):
    if num == []:
        return 0
    return num[0]+2*binaryToDecimal(num[1:])
    #takes first component and adds it to the next value times two and so on
    #cuz thats how binary works
    #if its a 0 it isnt added if its a one its added


# Given an R2L formatted number, return an R2L equivalent to num + 1
# If you need to increase the length, do so. Again, watch out for 0
def incrementBinary(num):
    if num==[]:
        return [1]
    if num[0]==0:
        return[1] + num[1:]
    else:
        return [0] + incrementBinary(num[1:])
    #if its empty or 0 return one
    #if the first value is zero add one to first value, then add the rest (no carrying over needed)
    #if the first value not zero, must carry over, so we make it 0 and move to next to see if it needs to be 1 or 0.
    

# Given 2 R2L numbers, return their sum.
## You MUST implement recursively the algorithm for bit-by-bit addition as taught in class,
## you may NOT do something like decimalToBinary( binaryToDecimal(num1) + binaryToDecimal(num2) ).
# Make sure to figure out what to do when num1 and num2 aren't of the same length!
# (and be sure you can add [] and [0])
## Tip: Try this on paper before typing it up
def addBinary(num1, num2):
    def add(n1,n2):
        if n1==[] and n2!=[]:
            return [n2[0]] + add(n1[:], n2[1:])
        if n2==[] and n1!=[]:
            return [n1[0]] + add(n1[1:], n2[:])
        if n1==[] and n2==[]:
            return []
        return [n1[0]+n2[0]] + add(n1[1:],n2[1:])
    #adds the two lists together

    def simple(p):
        if p==[]:
            return []
        if p[0]==0:
            return [0] + simple(p[1:])
        if p[0]==1:
            return [1] + simple(p[1:])
        else:
            return [0] + simple(incrementBinary(p[1:]))
    #then simplifies it. if it has 2's it carries over.
    #e.g. [0,1,2] becomes [0,1,0,1]
    
    l = add(num1,num2)

    return simple(l)
