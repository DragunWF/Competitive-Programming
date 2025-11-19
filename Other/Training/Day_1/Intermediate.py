import sys
from time import sleep

def solve() -> None:
    sys.stdout.write("N (NxN matrix): ")
    N = int(sys.stdin.readline())
    matrix = create_matrix(N)
    visited = create_visited_map(N)
    spiral_order_output = []

    # Traversal starts from the right
    traversals = {"right": True, "left": False, "down": False, "up": False}
    traversal_count = 0
    row, column = 0, 0
    while traversal_count < N * N:
        # Uncomment for debugging
        # debug_print_visited(visited)

        visited[row][column] = True
        spiral_order_output.append(matrix[row][column])
        traversal_count += 1

        # Check if traversal has reaches its corner
        if (column + 1 >= N or visited[row][column + 1]) and traversals["right"]:
            traversals["right"] = False
            traversals["down"] = True
        elif (row + 1 >= N or visited[row + 1][column]) and traversals["down"]:
            traversals["down"] = False
            traversals["left"] = True
        elif (column - 1 < 0 or visited[row][column - 1]) and traversals["left"]:
            traversals["left"] = False
            traversals["up"] = True
        elif (row - 1 < 0 or visited[row - 1][column]) and traversals["up"]:
            traversals["up"] = False
            traversals["right"] = True

        # Travel by either row or column depending on the direction
        if traversals["right"]:
            column += 1
        elif traversals["left"]:
            column -= 1
        elif traversals["down"]:
            row += 1
        elif traversals["up"]:
            row -= 1

    sys.stdout.write(f'Spiral Order: {" ".join(str(n) for n in spiral_order_output)}')


def create_matrix(n: int) -> list[list[int]]:
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            sys.stdout.write(f"Row: {i} Column: {j} - ")
            row.append(int(sys.stdin.readline()))
        matrix.append(row)
    return matrix


def create_visited_map(n: int) -> list[list[bool]]:
    visited_map = []
    for i in range(n):
        visited_map.append([False for j in range(n)])
    return visited_map


def debug_print_visited(matrix: list[list[int]]) -> None:
    """
    This function is primarily used for debugging (sys functions will not be used)
    :param matrix:
    :return:
    """
    print("-" * 20)
    for row in matrix:
        print(row)
    print("-" * 20)
    sleep(0.25)


if __name__ == "__main__":
    solve()