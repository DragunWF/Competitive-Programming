# https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1], [1, 1]]
        if numRows <= len(triangle):
            return triangle[0:numRows]
        for i in range(1, numRows - 1):
            row = []
            for j in range(len(triangle[i]) + 1):
                if j == 0:
                    row.append(triangle[i][j])
                else:
                    if j >= len(triangle[i]):
                        row.append(triangle[i][-1])
                    else:
                        row.append(triangle[i][j] + triangle[i][j - 1])
            triangle.append(row)
        return triangle