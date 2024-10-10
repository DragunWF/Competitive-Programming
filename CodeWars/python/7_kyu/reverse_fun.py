# https://www.codewars.com/kata/566efcfbf521a3cfd2000056/train/python

def reverse_fun(n):
    output = "".join(n)
    for i in range(len(n)):
        output = reverse(output, i)
    return output

def reverse(n, start):
    arr = [n[i] for i in range(start, len(n))]
    original = "".join([n[i] for i in range(start)])
    arr.reverse()
    return f'{original}{"".join(arr)}'

# Test code
print(reverse_fun("012345"))