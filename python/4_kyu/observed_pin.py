# https://www.codewars.com/kata/5263c6999e0f40dee200059d/train/python
from rich import print  # For viewing purposes | Not complete


def get_pins(observed: str) -> list:
    length = len(observed)
    if length == 1:
        return get_combinations(observed)

    combos = [get_combinations(x) for x in observed]
    count = len(combos[0])
    for i in range(1, length):
        count *= len(combos[i])

    output, base = [], [0 for x in range(length)]
    for i in range(count):
        pin = ["" for x in range(length)]
        for j in range(length):
            pin[j] = combos[j][base[j]]
        for j in range(length):
            len_limit = len(combos[j])
            if base[j] + 1 != len_limit:
                base[j] += 1
            elif base[j] + 1 == len_limit:
                base[j] = 0
                continue
            break
        output.append("".join(pin))

    return ["".join(x) for x in output]


def get_combinations(n: str) -> list:
    if n == "0":
        return [n, "8"]

    pad = (("1", "2", "3"), ("4", "5", "6"), ("7", "8", "9"))
    output, limit = [], 3
    if n == "8":
        output.append("0")
    for i in range(limit):
        for j in range(limit):
            if n == pad[i][j]:
                output.append(pad[i][j])
                if j + 1 != limit:
                    output.append(pad[i][j + 1])
                if j - 1 >= 0:
                    output.append(pad[i][j - 1])
                if i + 1 != limit:
                    output.append(pad[i + 1][j])
                if i - 1 >= 0:
                    output.append(pad[i - 1][j])

    return output


def get_iterations(index: int, combinations: list) -> int:
    result = 0
    for i in range(len(combinations)):
        if index != i:
            if result == 0:
                result += len(combinations[i])
                continue
            result *= len(combinations[i])
    return result


def test():  # Not part of the solution
    # arr_test = ["339", "366", "399", "658", "636",
    #             "258", "268", "669", "668", "266",
    #             "369", "398", "256", "296", "259",
    #             "368", "638", "396", "238", "356",
    #             "659", "639", "666", "359", "336",
    #             "299", "338", "696", "269", "358",
    #             "656", "698", "699", "298", "236",
    #             "239"]
    # count_3 = 0
    # count_6 = 0
    # count_5 = 0
    # for num in arr_test:
    #     if num[0] == "3":
    #         count_3 += 1
    #     if num[0] == "6":
    #         count_6 += 1
    #     if num[1] == "6":
    #         count_5 += 1
    # print(f"3: {count_3}")
    # print(f"6: {count_6}")
    # print(f"5: {count_5}")

    # print(len(arr_test))
    # [length * " " for x in range(count)]
    print(get_pins('8'))
    print(get_pins('11'))
    print(get_pins('369'))


test()
