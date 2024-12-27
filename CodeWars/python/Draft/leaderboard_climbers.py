# https://www.codewars.com/kata/5f6d120d40b1c900327b7e22/train/python

def leaderboard_sort(leaderboard: list[str], changes: list[str]) -> list[str]:
    output = [*leaderboard]
    for change in changes:
        values = change.split(" ")
        name = values[0]
        movement = int(values[1])

        new_pos = leaderboard.index(name) + movement * -1
        output = []
    return output
