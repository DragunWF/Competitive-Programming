# https://www.codewars.com/kata/5946a0a64a2c5b596500019a/train/python

def split_and_add(numbers: list, n: int) -> list:
    output = [*numbers]
    for i in range(n):
        if len(output) == 1:
            break
        middle = len(output) // 2
        first_half = output[:middle]
        second_half = output[middle:]
        output = add_halves(first_half, second_half)
    return output


def add_halves(first_half: list, second_half: list) -> list:
    output = []
    if len(first_half) != len(second_half):
        output.append(second_half[0])
        for i in range(1, len(second_half)):
            output.append(first_half[i - 1] + second_half[i])
        return output

    for i in range(len(first_half)):
        output.append(first_half[i] + second_half[i])
    return output


def test() -> None:
    arr = [1, 2, 5, 7, 2, 3, 5, 7, 8]
    print(split_and_add(arr, 1))


if __name__ == "__main__":
    test()
