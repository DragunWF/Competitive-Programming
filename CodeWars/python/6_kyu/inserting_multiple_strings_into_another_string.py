# https://www.codewars.com/kata/52f3eeb274c7e693a600288e/train/python

def insert_at_indexes(phrase: str, word: str, indexes: list[int]) -> str:
    additional_length = 0
    for i in indexes:
        phrase = phrase[:i + additional_length] + \
            word + phrase[i + additional_length:]
        additional_length += len(word)
    return phrase


def test() -> None:
    # I really like codewars! It makes me really happy.
    print(insert_at_indexes(
        "I like codewars! It makes me happy.", " really", [1, 28]))


if __name__ == "__main__":
    test()
