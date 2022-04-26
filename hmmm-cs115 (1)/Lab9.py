# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Name    : Adam Woo
# Pledge  : I pledge my honor that I have abided by the Stevens Honor System.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Max:
#  Write a hmmm function that gets two numbers,
#   then prints the larger of the two.
#  Assumptions: Both inputs are any integers
Max = """
    00 read r1          #get inputs
    01 read r2
    02 copy r3 r1       #store inputs
    03 copy r4 r2
    04 jeqzn r1 11      #if r1==0 end
    05 jeqzn r2 09      #if r2==0 end
    06 addn r1 -1       #decrement r1 and r2 until one of them hits 0
    07 addn r2 -1       
    08 jumpn 04 
    09 write r3         #return
    10 jumpn 12         #skip to end
    11 write r4         #return
    12 halt             #end
"""


# Power:
#  Write a hmmm function that gets two numbers,
#   then prints (No.1 ^ No.2).
#  Assumptions: No.1 is any integer, No.2 >= 0
Power = """
    00 read r1      #gets inputs
    01 read r2
    02 setn r3 1    #result = 1
    03 jeqzn r2 07  #if r2 0 go to end
    04 mul r3 r3 r1 #multiplies r1
    05 addn r2 -1   #takes away one from r2
    06 jumpn 03     #loop up to 03
    07 write r3     #return result
    08 halt
"""


# Fibonacci
#  Write a hmmm function that gets one number,
#   then prints the No.1st fibonacci number.
#  Assumptions: No.1 >= 0
#  Hint: You really don't want to implement
#   recursion in hmmm, try to find an
#   iterative method to compute your goal.
#  Tests: f(2) = 1
#         f(5) = 5
#         f(9) = 34
Fibonacci = """
    00 read r1          #get input
    
    01 setn r2 0        #set r2 to 0
    02 setn r3 1        #set r3 to 1
    03 setn r4 0        #set result(r4) to 0
    04 copy r5 r1       #makes r5 = r1 -1
    05 addn r5 -1
    
    06 jeqzn r1 15      #if r1==0 go to XX (return 0)
    07 jeqzn r5 18      #if r1==1 go to YY (return 1)
                        #everything after is if r1 >= 2

    08 addn r1 -1
    09 jeqzn r1 21      #jump to AA if r1==0
    10 add r4 r3 r2     #adds two nums
    11 addn r1 -1       #decrement r1
    12 copy r2 r3       #shift the addends up to next
    13 copy r3 r4
    14 jumpn 09         #loop up
    
    15 setn r1 0        #return 0 if r1==0
    16 write r1
    17 jumpn 22

    18 setn r1 1        #return 1 if r1==1
    19 write r1
    20 jumpn 22

    21 write r4

    22 halt
"""


# ~~~~~ Running ~~~~~~
import hmmm
import importlib

runThis = Fibonacci
# Change to the function you want to run
doDebug = True # Change to turn debug mode on/off

# call main() from the command line to run the program again
def main(runArg = runThis, debugArg = doDebug):
    importlib.reload(hmmm)
    hmmm.main(runArg, debugArg)

if __name__ == "__main__" : 
    main()


