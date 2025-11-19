# https://www.codewars.com/kata/525dfedb5b62f6954d000006/train/python

def score_throws(radii: list[int]) -> int:
    if not radii:
        return 0
    points = 0
    all_radii_less_than_5 = True
    for score in radii:
        if 5 <= score <= 10:
            points += 5
            all_radii_less_than_5 = False
        elif score < 5:
            points += 10
        else:
            all_radii_less_than_5 = False
    if all_radii_less_than_5:
        points += 100
    return points


def test() -> None:
    print(score_throws([1, 5, 11]))  # =>  15
    print(score_throws([15, 20, 30]))  # =>  0
    print(score_throws([1, 2, 3, 4]))  # =>  140


if __name__ == "__main__":
    test()
