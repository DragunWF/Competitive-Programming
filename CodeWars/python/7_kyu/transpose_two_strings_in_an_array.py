# https://www.codewars.com/kata/581f4ac139dc423f04000b99/train/python

def transpose_two_strings(arr: list[str]) -> str:
    output = []
    for i in range(max(len(arr[0]), len(arr[1]))):
        first_str = arr[0][i] if i < len(arr[0]) else " "
        second_str = arr[1][i] if i < len(arr[1]) else " "
        output.append(f"{first_str} {second_str}")
    return "\n".join(output)
