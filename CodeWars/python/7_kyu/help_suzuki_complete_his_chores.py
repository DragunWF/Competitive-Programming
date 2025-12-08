# https://www.codewars.com/kata/584dc1b7766c2bb158000226


def chore_assignment(chores: list[int]) -> list[int]:
    output = []
    start_index = 0
    end_index = -1
    chores.sort()
    while start_index < len(chores) // 2:
        output.append(chores[start_index] + chores[end_index])
        start_index += 1
        end_index -= 1
    output.sort()
    return output


def test() -> None:
    # Expected: [7, 8, 8, 10, 10, 11]
    print(chore_assignment([1, 5, 2, 8, 4, 9, 6, 4, 2, 2, 2, 9]))


if __name__ == "__main__":
    test()
