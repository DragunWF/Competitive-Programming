# https://leetcode.com/problems/pascals-triangle-ii/description/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = [[1], [1, 1]]
        if rowIndex < len(triangle):
            return triangle[rowIndex]
        for i in range(1, rowIndex):
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
        return triangle[rowIndex]