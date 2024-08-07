# https://www.codewars.com/kata/57cff961eca260b71900008f/train/python

def is_vow(inp):
    vowels = {ord('a'): 'a', ord('e'): 'e', ord('i'): 'i',
              ord('u'): 'u', ord('o'): 'o'}
    output = []
    for num in inp:
        output.append(vowels[num] if num in vowels else num)
    return output
