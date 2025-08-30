# https://www.codewars.com/kata/5b4e474305f04bea11000148/train/python

def digits(num: int) -> list[int]:
    num_list = [int(n) for n in str(num)]
    length = len(num_list)
    output = []
    for i in range(length):
        for j in range(i + 1, length):
            output.append(num_list[i] + num_list[j])
    return output


def test() -> None:
    print(digits(12345))


if __name__ == "__main__":
    test()
