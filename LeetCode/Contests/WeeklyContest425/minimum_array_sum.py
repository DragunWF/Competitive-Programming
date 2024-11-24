# https://leetcode.com/contest/weekly-contest-425/problems/minimum-array-sum/description/

# Not Finished

from typing import List


class Solution:
    def minArraySum(self, nums: List[int], k: int, op1: int, op2: int) -> int:
        return min(self.op1_first(nums, k, op1, op2),
                   self.op2_first(nums, k, op1, op2))

    def op2_first(self, nums: List[int], k: int, op1: int, op2: int) -> int:
        n = len(nums)
        arr_copy = [*nums]
        if op2 > 0:
            arr_copy.sort()
            for i in range(n):
                if arr_copy[i] >= k:
                    arr_copy[i] -= k
                    op2 -= 1
                    if op2 <= 0:
                        break
        print(arr_copy)
        if op1 > 0:
            arr_copy.sort(reverse=True)
            for i in range(n):
                if arr_copy[i] != 1:
                    arr_copy[i] = (arr_copy[i] / 2).__ceil__()
                    print(arr_copy[i], (arr_copy[i] / 2).__ceil__())
                    op1 -= 1
                    if op1 <= 0:
                        break
            arr_copy.sort(reverse=True)
        print(arr_copy)
        return sum(arr_copy)

    def op1_first(self, nums: List[int], k: int, op1: int, op2: int) -> int:
        n = len(nums)
        arr_copy = [*nums]
        if op1 > 0:
            arr_copy.sort(reverse=True)
            for i in range(n):
                arr_copy[i] = (arr_copy[i] / 2).__ceil__()
                op1 -= 1
                if op1 <= 0:
                    break
            arr_copy.sort(reverse=True)
        if op2 > 0:
            arr_copy.sort()
            for i in range(n):
                if arr_copy[i] >= k:
                    arr_copy[i] -= k
                    op2 -= 1
                    if op2 <= 0:
                        break
        return sum(arr_copy)


if __name__ == '__main__':
    sol = Solution()
    nums = [5, 3, 2, 7]
    k = 4
    op1 = 4
    op2 = 3
    print(sol.minArraySum(nums, k, op1, op2))  # Expected: 4
