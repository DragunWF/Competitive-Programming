# https://leetcode.com/problems/spiral-matrix/description/

from typing import List
from time import sleep  # Testing
from rich import print  # Testing #2


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        limit = m * n
        traversed = [[False for i in range(n)] for i in range(m)]
        visited = []
        traversalCount = 0
        row, column = 0, 0
        # Directions on which way to go
        left, right, up, down = False, True, False, False
        while traversalCount < limit:
            traversed[row][column] = True
            visited.append(matrix[row][column])
            traversalCount += 1
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
                if row + 1 >= m or traversed[row + 1][column]:
                    down = False
                    left = True
                    column -= 1
                else:
                    row += 1
        return visited


if __name__ == "__main__":
    # Test part, not part of the solution
    print(Solution().spiralOrder([[1, 2, 3, 4],
                                  [5, 6, 7, 8],
                                  [9, 10, 11, 12],
                                  [13, 14, 15, 16],
                                  [17, 18, 19, 20],
                                  [21, 22, 23, 24]]))
