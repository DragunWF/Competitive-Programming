# https://www.codewars.com/kata/59fca81a5712f9fa4700159a

def to_binary(num):
    output = ""
    for i in range(8):
        output += str(num % 2)
        num //= 2
    return int(output[::-1])
