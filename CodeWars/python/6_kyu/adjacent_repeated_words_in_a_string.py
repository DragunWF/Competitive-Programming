# https://www.codewars.com/kata/5245a9138ca049e9a10007b8/train/python

def count_adjacent_pairs(s: str) -> str:
    words = s.lower().split(" ")
    prev = {"word": None, "count": 0}
    adjacent_pairs = 0
    for word in words:
        if word != prev["word"]:
            prev["count"] = 1
        else:
            prev["count"] += 1
        if prev["count"] == 2:
            adjacent_pairs += 1
        prev["word"] = word
    return adjacent_pairs


def test() -> None:
    # Expected: 2
    print(count_adjacent_pairs("dog dog dog cat cat"))

    # Expected: 0
    print(count_adjacent_pairs("Jack Smith"))


if __name__ == "__main__":
    test()
