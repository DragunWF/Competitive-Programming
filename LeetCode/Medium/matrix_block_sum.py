# https://leetcode.com/problems/matrix-block-sum/description/

from typing import List


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        output = []
        for i in range(len(mat)):
            row = []
            for j in range(len(mat[i])):
                row.append(self.matrixSum(mat, i, j, k))
            output.append(row)
        return output

    def matrixSum(self, mat: List[List[int]], i: int, j: int, k: int) -> int:
        cell_sum = 0
        for r in range(max(0, i - k), min(len(mat), i + k + 1)):
            for c in range(max(0, j - k), min(len(mat[i]), j + k + 1)):
                cell_sum += mat[r][c]
        return cell_sum


def test() -> None:
    solution = Solution()

    # [[12,21,16],[27,45,33],[24,39,28]]
    print(solution.matrixBlockSum(
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1
    ))

    # [[45,45,45],[45,45,45],[45,45,45]]
    print(solution.matrixBlockSum(
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2
    ))


if __name__ == "__main__":
    test()
