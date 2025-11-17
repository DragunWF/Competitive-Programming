number = input()
digit_sum = 0
for digit in number:
    digit_value = int(digit)
    if digit_value % 2 == 0:
        digit_sum += digit_value
print(digit_sum)
