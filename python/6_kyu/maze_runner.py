# https://www.codewars.com/kata/58663693b359c4a6560001d6/train/python

def maze_runner(maze: list[list[int]], directions: list[str]) -> str:
    current_pos, N = find_initial_position(maze), len(maze)
    for direction in directions:
        if direction in ("N", "S"):
            current_pos[1] += -1 if direction == "N" else 1
        else:
            current_pos[0] += -1 if direction == "W" else 1
        X, Y = current_pos[0], current_pos[1]
        if X >= N or Y >= N or X < 0 or Y < 0 or maze[Y][X] == 1:
            return "Dead"
        elif maze[Y][X] == 3:
            return "Finish"
    return "Lost"


def find_initial_position(maze: list[list[int]]) -> list[int, int]:
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] == 2:
                return [x, y]


def test():
    # Not part of the solution, just testing
    print(maze_runner([[1, 1, 1, 1, 1, 1, 1],
                       [1, 0, 0, 0, 0, 0, 3],
                       [1, 0, 1, 0, 1, 0, 1],
                       [0, 0, 1, 0, 0, 0, 1],
                       [1, 0, 1, 0, 1, 0, 1],
                       [1, 0, 0, 0, 0, 0, 1],
                       [1, 2, 1, 0, 1, 0, 1]],
                      ["N", "N", "N", "N", "N", "E", "E", "E", "E", "E"]))
    # Finish should equal dead
    print(maze_runner([[0, 0, 2, 0, 1],
                       [0, 0, 0, 0, 0],
                       [1, 1, 1, 0, 1],
                       [1, 0, 1, 0, 0],
                       [0, 1, 0, 3, 0]],
                      ['N', 'E', 'S', 'W', 'E',
                       'W', 'N', 'W', 'W', 'W',
                       'N', 'W', 'S', 'N', 'S',
                       'N', 'N', 'E', 'N', 'W',
                       'W', 'S', 'N', 'S', 'W']))


if __name__ == "__main__":
    test()
