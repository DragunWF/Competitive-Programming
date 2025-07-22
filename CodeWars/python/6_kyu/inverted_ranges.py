# https://www.codewars.com/kata/60db06ded6c39e002ee35910/train/python

def inverted_ranges(ranges: list[tuple[int, int]]) -> list[tuple]:
    MIN, MAX = 0, 100

    taken_numbers = set()
    for pair in ranges:
        for i in range(pair[0], pair[1] + 1):
            taken_numbers.add(i)

    inverted_ranges = []
    current_range = []
    for n in range(MIN, MAX + 1):
        if not n in taken_numbers:
            current_range.append(n)
        else:
            if len(current_range) >= 1 and n - 1 != current_range[-1]:
                min_num = current_range[0]
                max_num = current_range[-1]
                inverted_ranges.append(
                    (min_num, max_num)
                )
                current_range.clear()
    if current_range:
        inverted_ranges.append((current_range[0], current_range[-1]))
    return inverted_ranges


def test() -> None:
    print(inverted_ranges([(25, 75), (98, 99)]))


if __name__ == "__main__":
    test()
