def solve() -> None:
    print("-" * 30)
    n = input_num("N: ")
    shift_list = input_integer_list(n)
    plaintext = input("Plaintext: ")

    print("-" * 30)
    print_encrypted_text(plaintext, shift_list)
    print("-" * 30)


def input_integer_list(n: int) -> list[int]:
    try:
        num_list = list(map(int, input("N Separated Integers: ").split(" ")))
        if len(num_list) != n:
            print(f"Number of integers entered does not match N! ({n})")
            return input_integer_list(n)
        return num_list
    except ValueError:
        print("Invalid integer list! All must be numbers and must be within the range of -25 to 25")
        return input_integer_list(n)


def input_num(input_str: str) -> int:
    try:
        return int(input(input_str))
    except ValueError:
        print("Input must be numeric")
        return input_num(input_str)


def print_encrypted_text(plaintext: str, shift_list: list[int]) -> None:
    lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    encrypted_text = ""
    current_shift_index = 0
    for char in plaintext:
        shift = shift_list[current_shift_index]
        if char.isalpha():
            if char.islower():
                encrypted_text += lowercase_letters[(lowercase_letters.index(char) + shift) % 26]
            else:
                encrypted_text += uppercase_letters[(uppercase_letters.index(char) + shift) % 26]
            current_shift_index = (current_shift_index + 1) % len(shift_list)
        else:
            encrypted_text += char
    print(encrypted_text)


if __name__ == "__main__":
    solve()