# https://www.codewars.com/kata/64b7bcfb0ca7392eca9f8e47

def fair_swap(list1: list[int], list2: list[int]) -> set:
    output = set()
    for first_num in list1:
        for second_num in list2:
            first_sum = sum(list1) - first_num + second_num
            second_sum = sum(list2) - second_num + first_num
            if first_sum == second_sum:
                output.add((first_num, second_num))
    return output


def test() -> None:
    print(fair_swap([1, 1], [2, 2]))  # ➞ {(1, 2)}
    print(fair_swap([1, 2], [2, 3]))  # ➞ {(1, 2), (2, 3)}
    print(fair_swap([2], [1, 3]))  # ➞ {(2, 3)}
    print(fair_swap([2, 3, 4], [11, 4, 1]))  # ➞ set()


if __name__ == "__main__":
    test()
