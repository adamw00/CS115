# Adapted by Dominick DiMaggio for Prof. Nicolosi's CS 115 at Stevens Institute of Technology, 2020

##########################################
# Name: Adam Woo
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
##########################################

# Import reduce from the functools package
from functools import reduce

#######################################################################################
# Task 1: Use reduce to determine if all elements in a boolean list are true
def all_true(lst):
    # TODO: Implement
    def isTrue(a,b):
        return a and b
    return (reduce(isTrue, lst))


#######################################################################################
# Task 1.1: Use reduce to determine if AT LEAST one element in a boolean list is true
# Hint: Should be very similar to the above function
def one_true(lst):
    # TODO: Implement
    def isOneTrue(a,b):
        return a or b
    return (reduce(isOneTrue, lst))
            
#######################################################################################
# Task 2: Use map and reduce to return how many elements are True in a boolean list
def count_true(lst):
    # TODO: Implement
    def add(a,b):
        return a+b
    return reduce(add,lst)
    
    
# This function is provided for you
# Gets a list of strings through the command line
# Input is accepted line-by-line
def getInput():
    lst = []
    txt = input()

    while(len(txt) != 0):
        lst.append(txt)
        txt = input()

    return lst

# Task 3: Get the longest string in the list using map and reduce, and print it out
# 'strings' is a list of input strings e.g. [ 'hello', 'world' ]
# Hint: The 'map' part of your program should take a string s into a length-2 list [len(s), s].
def getLongestString():
    strings = getInput()
    # TODO: Implement
    def find(a,b):
        if len(a) < len(b):
            return b
        else:
            return a
    if len(strings) == 0:
        return strings[0]
    else:
        return reduce(find, strings)
    

