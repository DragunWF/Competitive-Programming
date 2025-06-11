# https://www.codewars.com/kata/583ef2456e39941f810001c5/train/python

def duplicate_or_unique(arr: list[int]) -> int:
    counts = {}

    for num in arr:
        counts[num] = counts.get(num, 0) + 1

    unique_nums = []
    duplicate_nums = []

    for num, count in counts.items():
        if count == 1:
            unique_nums.append(num)
        else:
            duplicate_nums.append(num)
        if len(unique_nums) > 1 and len(duplicate_nums) == 1:
            return duplicate_nums[0]
        if len(duplicate_nums) > 1 and len(unique_nums) == 1:
            return unique_nums[0]

    return unique_nums[0] if len(unique_nums) == 1 else duplicate_nums[0]


def test() -> None:
    print(duplicate_or_unique([1, 2, 3, 6, 5, 4, 1]))  # 1
    print(duplicate_or_unique([1, 2, 3, 1, 2, 3, 4]))  # 4


if __name__ == "__main__":
    test()


# Original Solution

# def duplicate_or_unique(arr: list[int]) -> int:
#     return find_unique(arr) if is_duplicate_type(arr) else find_duplicate(arr)


# def is_duplicate_type(arr: list[int]) -> bool:
#     return len(arr) - len(set(arr)) != 1


# def find_duplicate(arr: list[int]) -> int:
#     seen = set()
#     for number in arr:
#         if number in seen:
#             return number
#         seen.add(number)


# def find_unique(arr: list[int]) -> int:
#     from collections import Counter  # Lazy Initialization
#     counter = Counter(arr)
#     for number in counter:
#         if counter[number] == 1:
#             return number
