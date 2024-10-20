# https://www.codewars.com/kata/564d0490e96393fc5c000029/train/python

def coin_combo(cents: int) -> list[int]:
    coins, change = (1, 5, 10, 25), [0, 0, 0, 0]
    for i in range(len(coins) - 1, -1, -1):
        change[i] = cents // coins[i]
        cents -= coins[i] * change[i]
    return change
