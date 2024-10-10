# https://www.codewars.com/kata/65c0161a2380ae78052e5731/train/python

def stone_pick(arr):
    inventory = {"Cobblestone": 0, "Sticks": 0}
    for item in arr:
        if item == "Sticks" or item == "Cobblestone":
            inventory[item] += 1
        elif item == "Wood":
            inventory["Sticks"] += 4
    return min(inventory["Cobblestone"] // 3, inventory["Sticks"] // 2)
