# https://www.codewars.com/kata/6a784d563bfd7732517d9832/train/python

def vertical(words: list[str]) -> str:
    if not words:
        return ""

    max_len = max(len(word) for word in words)
    output = []
    for i in range(max_len):
        line = []
        for word in words:
            if i < len(word):
                line.append(word[i])
            else:
                line.append(" ")
        output.append(" ".join(line).rstrip())
    return "\n".join(output)


def test() -> None:
    print(vertical(["hi", "world", "yo"]))


if __name__ == "__main__":
    test()
