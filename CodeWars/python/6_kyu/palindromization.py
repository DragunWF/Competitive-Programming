# https://www.codewars.com/kata/5840107b6fcbf56d2000010b/train/python

def palindromization(elements: list, n: int) -> str:
    if not elements or n < 2:
        return "Error!"

    start = 0
    end = -1
    i = 0
    output = ["" for i in range(n)]
    while "" in output:
        element = elements[i]
        output[start] = element
        output[end] = element
        i += 1
        start += 1
        end -= 1
        if i >= len(elements):
            i = 0
    return "".join(output)


def test() -> None:
    print(palindromization("123", 5))


if __name__ == "__main__":
    test()
