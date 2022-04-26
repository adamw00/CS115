# Created by Prof. Nicolosi & Dominick DiMaggio for CS 115 at Stevens Institute of Technology, 2020

##########################################
# Name: Adam Woo
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
##########################################
from math import floor

######################################################################
# Task 1: Given an 8-digit decimal number representing the date,
#         calculate the day of the week
# Input: 8-digit decimal number in the format of YYYYMMDD
# Saturday: 0, Sunday: 1... Friday: 6  
# Hint: Look at Zeller's congruence.
#       The floor() function may be helpful. (Ex: floor(5.5) = 5)

def getWeekday(timestamp):
    # TODO: Implement
    q = (timestamp%10000)%100
    m = ((timestamp%10000)/100)
    y = (timestamp/10000)
    K = (y%100)
    J = (y/100)
    return int((q+(floor((13*(m+1))/5))+K+floor(K/4)+floor(J/4)-2*J)%7)
    
######################################################################
# Task 2: For this task, you will create an encoder and decoder
#         for a Caesar cipher using the map function.
# You may find this website helpful:
# https://cryptii.com/pipes/caesar-cipher

######################################################################
# This provided helper function may be useful
# Input: List of ASCII values (Ex: [72, 69, 76, 76, 79])
# Output: String (Ex. 'HELLO')     ('H   E   L   L   O')
def asciiToString(asciiList):
    return ''.join(map(chr, asciiList))


######################################################################
# Encoder
# Input: A string value with all capital letters (leave everything
#        else as-is) and a shift value (Ex. HELLO WORLD, 3)
# Output: An encoded string            (Ex. KHOOR ZRUOG)
# Hint: The ord() function converts single-character strings to ASCII
def caesarEncoder(str, shift):
    # TODO: Implement
    def pp(a):
        return a
    charList = list(map(pp,str))

    
    def convert(x):
        c = ord(x)+shift
        if c > 90:
            c-=26
        if x==' ':
            return ord(x)
        else:
            return c
    aList = list(map(convert,charList))

    
    return asciiToString(aList)

######################################################################
# Decoder
# Input: A string value with all capital letters (leave everything
#        else as-is) and a shift value (Ex. KHOOR ZRUOG, 3)
# Output: A decoded string             (Ex. HELLO WORLD)
# Hint: The chr() function converts ASCII to a single-character string
def caesarDecoder(str, shift):
    def pp(a):
        return a
    charList = list(map(pp,str))

    
    def convert(x):
        c = ord(x)-shift
        if c < 65:
            c+=26
        if x==' ':
            return ord(x)
        else:
            return c
    aList = list(map(convert,charList))

    
    return asciiToString(aList)

    
