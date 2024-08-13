# https://www.codewars.com/kata/57f625992f4d53c24200070e/train/python

def bingo(ticket: list, win: int) -> str:
    mini_wins = 0
    for item in ticket:
        if any([ord(char) == item[1] for char in item[0]]):
            mini_wins += 1
    return "Winner!" if mini_wins >= win else "Loser!"
