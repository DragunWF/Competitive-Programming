# https://www.codewars.com/kata/5966847f4025872c7d00015b/train

def average_string(s: str):
    words = s.split(" ")
    numbers = ("zero", "one", "two", "three", "four",
               "five", "six", "seven", "eight", "nine")
    total = 0
    for word in words:
        if not word in numbers:
            return "n/a"
        total += numbers.index(word)
        valid = True
    return numbers[total // len(words)]


# Test code
print(average_string("zero nine five two"))
