# https://www.codewars.com/kata/53921994d8f00b93df000bea/train/python

def content_weight(bottle_weight: int, scale: str) -> int:
    scale_values = scale.split(" ")
    scale_weight = int(scale_values[0]) + 1
    scale_direction = scale_values[-1]

    individual_weight = bottle_weight // scale_weight
    return individual_weight if scale_direction == "smaller" else bottle_weight - individual_weight
