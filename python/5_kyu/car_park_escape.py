# https://www.codewars.com/kata/591eab1d192fe0435e000014/train/python

def escape(carpark: list[list[int]]) -> list[str]:
    EXIT_POS, current_pos = get_exit_pos(carpark), find_initial_pos(carpark)
    directions = []

    # Traverses through the car park
    while current_pos != EXIT_POS:
        row, col = current_pos
        staircase = find_staircase(carpark[row])

        # Decision making on which directions to take
        if staircase > col:
            directions.append(f"R{staircase - col}")
        elif staircase < col:
            directions.append(f"L{col - staircase}")
        else:
            # Increment previous "Down" direction if the staircase is on the same tile
            directions[-1] = f"D{int(directions[-1][1:]) + 1}"
        if current_pos[0] < EXIT_POS[0]:
            current_pos[0] += 1
            # If the stair is not on the same position as the previous floor then add a new direction
            if directions[-1][0] != "D":
                directions.append("D1")
        current_pos[1] = staircase

    return directions


def find_staircase(floor: list[int]) -> list[int, int]:
    for i, num in enumerate(floor):
        if num == 1:
            return i
    return len(floor) - 1


def find_initial_pos(carpark: list[list[int]]) -> list[int, int]:
    for row in range(len(carpark)):
        for col in range(len(carpark[row])):
            if carpark[row][col] == 2:
                return [row, col]


def get_exit_pos(carpark: list[list[int]]) -> list[int, int]:
    LAST_ROW = len(carpark) - 1
    return [LAST_ROW, len(carpark[LAST_ROW]) - 1]  # Last row and column


def test():
    # Not part of the solution, just testing
    print(escape([[1, 0, 0, 0, 2],
                  [0, 0, 0, 0, 0]]))  # ["L4", "D1", "R4"]
    print(escape([[2, 0, 0, 1, 0],
                  [0, 0, 0, 1, 0],
                  [0, 0, 0, 0, 0]]))  # ["R3", "D2", "R1"]


if __name__ == '__main__':
    test()
