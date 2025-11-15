# https://www.codewars.com/kata/525f039017c7cd0e1a000a26

def palindrome_chain_length(n: int) -> int:
    steps = 0
    current_num = n
    while not is_palindrome(current_num):
        reversed_num = int(str(current_num)[::-1])
        current_num = current_num + reversed_num
        steps += 1
    return steps


def is_palindrome(n: int) -> bool:
    str_num = str(n)
    return str_num[::-1] == str_num


def test() -> None:
    # Expected: 4
    print(palindrome_chain_length(87))


if __name__ == "__main__":
    test()
