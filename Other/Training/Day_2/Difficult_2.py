import sys


def solve() -> None:
    grid = [
        [0, 0, 0, 1, 0],
        [0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0]
    ]
    print_grid(grid)
    start = [int(input("Start (Row): ")), int(input("Start (Column): "))]
    end = [int(input("End (Row): ")), int(input("End (Column): "))]
    print(f"Path Exists: {is_path_exists(grid, start, end)}")


def is_path_exists(grid: list[list[int]], start: list, end: list) -> bool:
    visited = create_visited_map(grid)

    row_length = len(grid)
    column_length = len(grid[0])

    # To take advantage of reference type modifications instead of primitives
    is_path_found = [False]

    def traverse(current_pos: list, is_path_found: list[bool]) -> bool:
        if current_pos[0] == end[0] and current_pos[1] == end[1]:
            is_path_found[0] = True
            return

        visited[current_pos[0]][current_pos[1]] = True
        if current_pos[0] + 1 < row_length and not visited[current_pos[0] + 1][current_pos[1]]:
            traverse([current_pos[0] + 1, current_pos[1]], is_path_found)
        if current_pos[0] - 1 >= 0 and not visited[current_pos[0] - 1][current_pos[1]]:
            traverse([current_pos[0] - 1, current_pos[1]], is_path_found)
        if current_pos[1] + 1 < column_length and not visited[current_pos[0]][current_pos[1] + 1]:
            traverse([current_pos[0], current_pos[1] + 1], is_path_found)
        if current_pos[1] - 1 >= 0 and not visited[current_pos[0]][current_pos[1] - 1]:
            traverse([current_pos[0], current_pos[1] - 1], is_path_found)

    traverse(start, is_path_found)
    return is_path_found[0]


def create_visited_map(grid: list[list[int]]) -> list[list[bool]]:
    visited = []
    for row in grid:
        visited.append([bool(item) for item in row])
    return visited


def print_grid(grid: list[list[int]]) -> None:
    print("+ ---- Grid ---- +")
    for row in grid:
        print(row)
    print("+ " + ("-" * 14) + " +")


if __name__ == "__main__":
    solve()
