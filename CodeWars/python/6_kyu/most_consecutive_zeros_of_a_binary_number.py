# https://www.codewars.com/kata/59decdf40863c76ae3000080/train/python

def max_consec_zeros(s: str) -> str:
    num_map = (
        "Zero", "One", "Two", "Three", "Four", "Five",
        "Six", "Seven", "Eight", "Nine", "Ten",
        "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen",
        "Sixteen", "Seventeen", "Eighteen", "Nineteen", "Twenty"
    )
    binary = bin(int(s))[2:]
    max_consecutive_zero_count = 0
    consecutive_zero_count = 0
    for digit in binary:
        if digit == "0":
            consecutive_zero_count += 1
            if consecutive_zero_count > max_consecutive_zero_count:
                max_consecutive_zero_count = consecutive_zero_count
        else:
            consecutive_zero_count = 0
    return num_map[max_consecutive_zero_count]


def test() -> None:
    print(max_consec_zeros("9"))  # Two
    print(max_consec_zeros("8192"))  # Thirteen


if __name__ == "__main__":
    test()
