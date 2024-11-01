# https://www.hackerrank.com/challenges/any-or-all/problem

def is_palindrome(s: int) -> bool:
    char_arr = [*str(s)]
    char_arr.reverse()
    return s == int("".join(char_arr))

if __name__ == "__main__":
    input()
    arr = list(map(int, input().split(" ")))
    print(all([n >= 0 for n in arr]) and any([is_palindrome(n) for n in arr]))