# https://www.codewars.com/kata/58d76854024c72c3e20000de/train/python

def reverse_alternate(st: str):
    output = []
    words = [word for word in st.split(" ") if word]
    for i, word in enumerate(words):
        output.append(word[::-1] if (i + 1) % 2 == 0 else word)
    return " ".join(output)


def test():
    # Not part of the solution, just testing
    print(reverse_alternate("Hello there my   friend!"))


if __name__ == "__main__":
    test()
