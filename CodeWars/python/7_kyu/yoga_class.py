# https://www.codewars.com/kata/5c79c07b4ba1e100097f4e1a

def yoga(classroom: list[list[int]], poses: list[int]):
    total_pose_completions = 0
    for row in classroom:
        total_pose_completions += count_pose_completions(row, poses)
    return total_pose_completions


def count_pose_completions(row: list[int], poses: list[int]) -> None:
    total = 0
    row_sum = sum(row)
    for skill in row:
        for pose in poses:
            if skill + row_sum >= pose:
                total += 1
    return total


def test() -> None:
    classroom = [
        [1, 1, 0, 1],  # sum = 3
        [2, 0, 6, 0],  # sum = 8
        [0, 2, 2, 0],  # sum = 4
    ]
    poses = [4, 0, 20, 10]
    print(yoga(classroom, poses))
    print(yoga([
        [3, 2, 1, 3],
        [1, 3, 2, 1],
        [1, 1, 1, 2],
    ], [1, 7, 5, 9, 10, 21, 4, 3]))


if __name__ == "__main__":
    test()
