# https://www.codewars.com/kata/58b972cae826b960a300003e/python

def missing(nums: list[int], s: str):
    words = "".join(s.split(" "))
    output = ""
    for num in sorted(nums):
        if not (0 <= num < len(words)):
            return "No mission today"
        output += words[num]
    return output.lower()


def test() -> None:
    print(missing([5, 0, 3], "I Love You"))  # expected output: ivy


if __name__ == "__main__":
    test()
