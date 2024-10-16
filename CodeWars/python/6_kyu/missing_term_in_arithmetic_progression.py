# https://www.codewars.com/kata/52de553ebb55d1fca3000371/train/python

from collections import Counter


def find_missing(seq: list[int]) -> int:
    gaps = Counter([seq[i] - seq[i - 1] for i in range(1, len(seq))])
    diff_pair = find_pair(gaps)
    for i in range(1, len(seq)):
        if seq[i] - seq[i - 1] == diff_pair["mismatch"]:
            return seq[i - 1] + diff_pair["correct_gap"]


def find_pair(gaps: Counter):
    mismatch = None
    correct_gap = None
    for num in gaps:
        if gaps[num] == 1:
            mismatch = num
        else:
            correct_gap = num
    return {"mismatch": mismatch, "correct_gap": correct_gap}


def test():
    print(find_missing([1, 3, 5, 9, 11]))  # == 7


if __name__ == '__main__':
    test()
