# https://leetcode.com/problems/set-matrix-zeroes/description/

from copy import deepcopy

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        output = deepcopy(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    self.set_to_zero(output, i, j)
        
        for i in range(len(output)):
            for j in range(len(output[i])):
                matrix[i][j] = output[i][j]
    
    def set_to_zero(self, matrix: List[List[int]], i: int, j: int) -> None:
        for row in range(len(matrix)):
            matrix[row][j] = 0
        for k in range(len(matrix[i])):
            matrix[i][k] = 0