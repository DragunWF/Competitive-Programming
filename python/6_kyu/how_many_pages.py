# https://www.codewars.com/kata/622de76d28bf330057cd6af8/train/python

def amount_of_pages(summary):
    output = ""
    for i in range(1, summary + 1):
        output += str(i)
        if len(output) >= summary:
            return i


print(amount_of_pages(5))
