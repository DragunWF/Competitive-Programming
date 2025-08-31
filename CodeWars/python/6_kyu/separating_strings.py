# https://www.codewars.com/kata/5977ef1f945d45158d00011f/train/python

def sep_str(s: str) -> list:
    words = s.split(" ")
    row_count = max(len(word) for word in words)
    column_count = len(words)

    output = []
    for i in range(row_count):
        row = []
        for j in range(column_count):
            row.append(words[j][i] if i < len(words[j]) else "")
        output.append(row)

    return output


def test() -> None:
    print(sep_str("Just live life man"))


if __name__ == "__main__":
    test()
