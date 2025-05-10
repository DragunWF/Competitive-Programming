# https://www.codewars.com/kata/5a2d70a6f28b821ab4000004/train/python

def largest_sum(s: str) -> int:
    digit_groups = s.split("0")
    max_sum = 0
    for group in digit_groups:
        current_sum = sum([int(char) for char in group])
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum


def test() -> None:
    print(largest_sum("72102450111111090"))  # 11


if __name__ == "__main__":
    test()
