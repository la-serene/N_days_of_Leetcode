# Counting Money
# https://www.educative.io/courses/algorithms-coding-interviews-python/challenge-counting-money

"""
Given an infinite number of quarters ( 25 𝑐 𝑒 𝑛 𝑡 𝑠 ) (25cents) , dimes ( 10 𝑐 𝑒 𝑛 𝑡 𝑠 ) (10cents) ,
nickels ( 5 𝑐 𝑒 𝑛 𝑡 𝑠 ) (5cents) , and pennies ( 1 𝑐 𝑒 𝑛 𝑡 ) (1cent) , implement a function to calculate the
minimum number of coins to represent 𝑣 v cents.
"""


def find_min_coins(v, coins_available):
    """
    This function finds the minimum number of coins in O(n ^ 2).
    :param v: Total amount
    :param coins_available: Coins available in the machine
    :return: A list of total coins
    """

    lst_coin = []
    for i in reversed(coins_available):
        while i <= v:
            lst_coin.append(i)
            v -= i

    return lst_coin


def find_min_coins_optimized(v, coins_available):
    """
    This function finds the minimum number of coins in O(n).
    :param v: Total amount
    :param coins_available: Coins available in the machine
    :return: A list of total coins
    """

    lst_coin = []
    lo, hi = 0, len(coins_available) - 1
    coin = coins_available[hi]
    while lo <= hi:
        if coin <= v:
            lst_coin.append(coin)
            v -= coin
        else:
            hi -= 1
            coin = coins_available[hi]

    return lst_coin
