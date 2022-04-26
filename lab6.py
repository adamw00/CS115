####################################################################################
# Name: 
# Pledge: 
####################################################################################
# Lab 6: Recursion 2
# Demonstrate recursion as an algorithm design technique for the problem of 
# computing the (length of the) longest common subsequence of two given strings
#####################################################################################

##############################################################################
# Example: The longest common subsequence of "helllowo_rld" and "!helloabcworld!"
# is "helloworld", and it has a length of 10.
#
# Therefore LLCS("helllowo_rld", "!helloabcworld!") returns 10, and
# LCS("helllowo_rld", "!helloabcworld!") returns "helloworld"
##############################################################################

def LLCS(S1, S2):
    if not S1 or not S2:
        return 0
    
    x = S1[0]
    xtail = S1[1:]
    y = S2[0]
    ytail = S2[1:]

    if x == y:
        return 1 + LLCS(xtail, ytail)
    return max(LLCS(S1, ytail), LLCS(xtail, S2))
    

##############################################################################
# Instead of returning the length of the longest common substring, this task
# asks you to return the string itself.
##############################################################################
# Tip: You may find it helpful to copy your solution to LLCS and edit it
# to solve this problem
##############################################################################

def LCS(S1, S2):
    '''return the longest common subsequence (LCS) between strings S1 and S2'''

    
    if not S1 or not S2:
        return ""

    x = S1[0]
    xtail = S1[1:]
    y = S2[0]
    ytail = S2[1:]

    if x==y:
        return x + LCS(xtail, ytail)

    return max(LCS(S1, ytail), LCS(xtail, S2), key=len)


    
