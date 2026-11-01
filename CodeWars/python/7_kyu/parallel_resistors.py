# https://www.codewars.com/kata/5723b111101f5f905f0000a5/train/python

def resistor_parallel(*args) -> float:
    total = 0
    for resistor in args:
        total += 1 / resistor
    return 1 / total