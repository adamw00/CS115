#I pledge my honor that I have abided by the Stevens Honor System.
#Adam Woo
from random import randrange

def change(amount,coins):

    if not coins or amount <= 0:
        return []
    else:
        return min((change(amount - coin, coins) + [coin]
                    for coin in coins if amount >= coin), key=len)

def currency(num):
    return
