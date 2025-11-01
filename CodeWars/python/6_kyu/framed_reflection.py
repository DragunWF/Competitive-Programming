# https://www.codewars.com/kata/581331293788bc1702001fa6/train/python

def mirror(text: str) -> str:
    words = text.split(" ")
    max_len = max(len(word) for word in words)
    output = ["*" * (max_len + 4)]
    for word in words:
        line = "*"
        line += f" {word[::-1]} "
        line += " " * (max_len - len(word))
        line += "*"
        output.append(line)
    output.append("*" * (max_len + 4))
    return "\n".join(output)


def test() -> None:
    print(mirror("Hello World"))


if __name__ == "__main__":
    test()
