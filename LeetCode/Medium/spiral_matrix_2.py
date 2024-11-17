# https://leetcode.com/problems/spiral-matrix-ii/description/

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        limit = n * n
        traversed = [[False for i in range(n)] for i in range(n)]
        matrix = [[0 for i in range(n)] for i in range(n)]
        traversalCount = 0
        row, column = 0, 0
        # Directions on which way to go
        left, right, up, down = False, True, False, False
        cell_value = 1
        while traversalCount < limit:
            traversed[row][column] = True
            matrix[row][column] = cell_value
            traversalCount += 1
            cell_value += 1
            if right:
                if column + 1 >= n or traversed[row][column + 1]:
                    right = False
                    down = True
                    row += 1
                else:
                    column += 1
            elif left:
                if column - 1 < 0 or traversed[row][column - 1]:
                    left = False
                    up = True
                    row -= 1
                else:
                    column -= 1
            elif up:
                if row - 1 < 0 or traversed[row - 1][column]:
                    up = False
                    right = True
                    column += 1
                else:
                    row -= 1
            elif down:
                if row + 1 >= n or traversed[row + 1][column]:
                    down = False
                    left = True
                    column -= 1
                else:
                    row += 1
        return matrix