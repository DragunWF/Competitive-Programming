# https://www.codewars.com/kata/651bfcbcdb0e8b104175b97e

def pop_blocks(lst):
    new, has_adjacent, i = [], False, 0
    while i < len(lst):
        if not has_adjacent and not (i + 1 >= len(lst)) and lst[i] == lst[i + 1]:
            has_adjacent = True
            i += 2
            continue
        new.append(lst[i])
        i += 1
    return pop_blocks(new) if has_adjacent else new


# Not part of the solution
def test():
    test_cases = (["B", "B", "A", "C", "A", "A", "C"],
                  ["B", "B", "C", "C", "A", "A", "A"],
                  ["C", "A", "C"],
                  ['ab', 'ab', 'cd', 'cx', 'B'],
                  [])
    for test_case in test_cases:
        print(pop_blocks(test_case))


if __name__ == '__main__':
    test()
