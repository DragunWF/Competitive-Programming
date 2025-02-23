# https://www.codewars.com/kata/52705ed65de62b733f000064/train/python

def sort_list(sort_by: str, lst: list[dict]) -> list[dict]:
    data_len = len(lst)
    sorted_lst = [*lst]
    for i in range(data_len):
        is_sorted = True
        for j in range(data_len - 1):
            if sorted_lst[j + 1][sort_by] > sorted_lst[j][sort_by]:
                sorted_lst[j], sorted_lst[j +
                                          1] = sorted_lst[j + 1], sorted_lst[j]
                is_sorted = False
        if is_sorted:
            break
    return sorted_lst


def test() -> None:
    print(sort_list("a", [
        {"a": 1, "b": 3},
        {"a": 3, "b": 2},
        {"a": 2, "b": 40},
        {"a": 4, "b": 12}
    ]))


if __name__ == "__main__":
    test()
