# https://www.codewars.com/kata/58ae6ae22c3aaafc58000079/train/python

def permute_a_palindrome(input: str) -> bool:
    counter = create_counter(input)
    odd_char_count = 0
    for key in counter:
        if counter[key] % 2 != 0:
            odd_char_count += 1
    return odd_char_count <= 1


def create_counter(input: str) -> dict:
    output = {}
    for char in input:
        if char in output:
            output[char] += 1
        else:
            output[char] = 1
    return output


def test() -> None:
    print(permute_a_palindrome("madam"))  # True
    print(permute_a_palindrome("adamm"))  # True
    print(permute_a_palindrome("junk"))  # False


if __name__ == "__main__":
    test()
