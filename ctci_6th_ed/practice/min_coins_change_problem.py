"""
Topic: Dynamic Programming

Reference: https://interactivepython.org/runestone/static/pythonds/Recursion/DynamicProgramming.html

Given an amount and possible denominations, determine the fewest coins that can be used to change this amount

example: amount = 63
         denominations = [1, 5, 10, 21, 25, 50]

         Minimum number of coins needed to change 63 = 3 (21 + 21 + 21)

This problem can be solved using dynamic programming: bottom up and memoization approach

if the amount is A and number of denominations is D, the below approach takes O(A) space and O(A*D) runtime
"""


def min_coins(amount, denominations):
    min_coins_lst = [0] * (amount + 1)
    for i in range(1, amount + 1):
        for index, denomination in enumerate(denominations):
            if denomination <= i:
                if index == 0:
                    min_coins = 1 + min_coins_lst[i - denomination]
                else:
                    min_coins = min(min_coins, 1 + min_coins_lst[i - denomination])
        min_coins_lst[i] = min_coins
    return min_coins


def main():
    """ the main method """
    amount = 63
    denominations = [1, 5, 10, 21, 25, 50]
    print("Minimum number of coins needed to change {} is {}".format(amount, min_coins(amount, denominations)))


if __name__ == "__main__":
    main()
