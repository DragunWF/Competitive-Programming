def solve(matrix):
    arr_index, item_index = None, None
    for i in range(len(matrix)):
        if 1 in matrix[i]:
            arr_index = i
            item_index = matrix[i].index(1)
            break
    return abs((arr_index + 1 - 3)) + abs((item_index + 1 - 3))


def main():
    matrix = []
    for i in range(5):
        arr = tuple(map(int, input().split(" ")))
        matrix.append(arr)
    print(solve(matrix))


main()
