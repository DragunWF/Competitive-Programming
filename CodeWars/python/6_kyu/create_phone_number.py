# https://www.codewars.com/kata/525f50e3b73515a6db000b83

def create_phone_number(n):
    x, y, z = "", "", ""
    iteration = 0
    for number in n:
        if iteration > 5:
            z += str(number)
        elif iteration > 2:
            y += str(number)
        else:
            x += str(number)
        iteration += 1
    return f"({x}) {y}-{z}"
