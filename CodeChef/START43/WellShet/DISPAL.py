from string import ascii_lowercase as letters
from math import floor

# Me at the end of the competition:
# https://youtu.be/Q3gy8A0jY10?t=54


def is_palindrome(n, x):
    if x == 1 or n == 1:
        return True
    length_even = n % 2 == 0
    half_length = n // 2 + (1 if not length_even else 0)
    if x > half_length:
        return False
    return half_length % x != 1


def generate_half(unique, spaces_occupied, is_even, n_is_even):
    output = []
    local_unique = [*unique]

    if not n_is_even:
        local_unique.pop()

    for letter in local_unique:
        for i in range(spaces_occupied):
            output.append(letter)

    if not is_even:
        output.pop()

    return output


def generate_palindrome(n, x):
    if n <= 2 and x == 1:
        return "a" * n

    unique = []
    for i in range(x):
        unique.append(letters[i])

    half_length = n // 2
    n_is_even = n % 2 == 0
    first_half, second_half = [], []
    spaces_occupied = floor(half_length / x)
    for half in range(2):
        if half == 0:
            first_half = generate_half(unique, spaces_occupied,
                                       half_length % 2 == 0, n_is_even)
        else:
            second_half = generate_half(unique, spaces_occupied,
                                        half_length % 2 == 0, n_is_even)
    second_half.reverse()

    return f'{"".join(first_half)}{"" if n_is_even else unique[-1]}{"".join(second_half)}'


def main():
    t = int(input())
    for i in range(t):
        n, x = map(int, input().split(" "))
        print(generate_palindrome(n, x) if is_palindrome(n, x)
              else -1)


main()
