# https://www.codewars.com/kata/66fc9ca2e6d1d0e9cc2e4a4c/train/python

def count_streets(streets: list, drivers: list) -> list:
    output = []
    street_map = {}
    for i, street in enumerate(streets):
        street_map[street] = i
    for driver in drivers:
        output.append(abs(street_map[driver[0]] - street_map[driver[1]]) - 1)
    return output
