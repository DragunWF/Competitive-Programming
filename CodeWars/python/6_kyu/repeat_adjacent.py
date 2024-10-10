# https://www.codewars.com/kata/58b8dccecf49e57a5a00000e

def repeat_adjacent(st):
    big_groups, groups, temp = 0, [], ""
    for i, char in enumerate(st):
        if not temp or st[i - 1] == char:
            temp += char
        else:
            groups.append(temp)
            temp = char
    groups.append(temp)

    adjacent_groups, lock = 0, False
    for group in groups:
        if len(group) >= 2:
            adjacent_groups += 1
        else:
            adjacent_groups = 0
            lock = False
        if adjacent_groups >= 2 and not lock:
            big_groups += 1
            lock = True
    return big_groups

# Test code
print(repeat_adjacent("ccccoooooooooooooooooooooooddee"))
print(repeat_adjacent("ccccoodeffffiiighhhhhhhhhhttttttts"))