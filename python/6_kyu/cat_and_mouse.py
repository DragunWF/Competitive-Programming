# https://www.codewars.com/kata/57ee2a1b7b45efcf700001bf

def cat_mouse(x, j):
    pos = {"C": None, "m": None, "D": None }
    order = []
    for i, char in enumerate(x):
        if char in pos:
            pos[char] = i
            order.append(char)
    if len(order) < 3:
        return "boring without all three"
    
    is_dog_absent = order[1] != "D" or len(order) <= 2
    is_right = pos["m"] > pos["C"]
    if is_right and (pos["C"] + j + 1) >= pos["m"]:
        return "Caught!" if is_dog_absent else "Protected!"
    elif not is_right and (pos["C"] - j - 1) <= pos["m"]:
        return "Caught!" if is_dog_absent else "Protected!"
    
    return "Escaped!"
    
def test():
    test_cases = [["..C.....m...D", 5], # Caught
                  ['............C.............D..m...', 8], # Escape
                  ['.CD......m.', 1], # Escape
                  ["..C..D..m....", 5]] # Protected
    for case in test_cases:
        print(cat_mouse(case[0], case[1]))

if __name__ == "__main__":
    test()