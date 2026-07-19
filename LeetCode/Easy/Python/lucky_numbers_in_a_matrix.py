# https://leetcode.com/problems/lucky-numbers-in-a-matrix/

from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        columns = self.getColumns(matrix)
        lucky_numbers = []
        for i in range(len(matrix)):
            min_num = min(matrix[i])
            max_num = max(self.getColumnByNum(columns, min_num))
            if min_num == max_num:
                lucky_numbers.append(max_num)
        return lucky_numbers

    def getColumns(self, matrix: List[List[int]]) -> List[List[int]]:
        column_length = len(matrix[0])
        columns = []
        for i in range(column_length):
            column = []
            for j in range(len(matrix)):
                column.append(matrix[j][i])
            columns.append(column)
        columns.reverse()
        return columns

    def getColumnByNum(self, columns: List[List[int]], target: int) -> List[int]:
        for column in columns:
            for num in column:
                if num == target:
                    return column


def test() -> None:
    solution = Solution()
    print(solution.getColumns([[3, 7, 8], [9, 11, 13], [15, 16, 17]]))
    print(solution.luckyNumbers([[3, 7, 8], [9, 11, 13], [15, 16, 17]]))

    print(solution.getColumns([[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]))
    print(solution.luckyNumbers([[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]))


if __name__ == "__main__":
    test()
