# https://www.codewars.com/kata/5e8dd197c122f6001a8637ca/train/python

def remove_duplicate_ids(obj: dict[str, list]) -> dict:
    keys = sorted([int(key) for key in obj], reverse=True)
    seen = set()
    unique: dict[str, list] = {}
    for key in keys:
        str_key = str(key)
        unique[str_key] = []
        for item in obj[str_key]:
            if not item in seen:
                unique[str_key].append(item)
            seen.add(item)
    return unique


def test() -> None:
    item = {
        "1": ["F", "G"],
        "2": ["C"],
        "4": ["D"],
        "3": ["A", "B", "D"],
    }
    print(remove_duplicate_ids(item))


if __name__ == "__main__":
    test()
