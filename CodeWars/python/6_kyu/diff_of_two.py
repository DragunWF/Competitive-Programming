# https://www.codewars.com/kata/5340298112fa30e786000688/train/python

def twos_difference(lst: list[int]) -> list[int]:
    pairs: list[tuple[int, int]] = []
    lst.sort()
    for i, num in enumerate(lst):
        for j, other_num in enumerate(lst):
            if i == j:
                continue
            pair = (num, other_num)
            if not is_pair_exists(pairs, pair) and abs(num - other_num) == 2:
                pairs.append(pair)
    return pairs


def is_pair_exists(pairs: list[tuple[int, int]], pair: tuple[int, int]):
    return pair in pairs or (pair[1], pair[0]) in pairs


def test():
    # Not part of the solution, just testing
    print(twos_difference([1, 2, 3, 4]))  # [(1, 3), (2, 4)]


if __name__ == "__main__":
    test()
