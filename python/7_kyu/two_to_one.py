# https://www.codewars.com/kata/5656b6906de340bd1b0000ac

def longest(a1, a2):
    values, set = (a1, a2), []
    for i in range(2):
        for letter in values[i]:
            if letter not in set:
                set.append(letter)
    return "".join(sorted(set))
