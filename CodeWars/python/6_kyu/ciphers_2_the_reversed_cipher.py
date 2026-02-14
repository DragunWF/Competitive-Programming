# https://www.codewars.com/kata/59474c656ff02b21e20000fc

def encode(s: str) -> str:
    words = s.split(" ")
    encrypted_words = []
    for word in words:
        encrypted_words.append(f"{word[::-1][1:]}{word[-1]}")
    return " ".join(encrypted_words)


def test() -> None:
    print(encode("Hello World!"))  # "lleHo dlroW!"


if __name__ == "__main__":
    test()
