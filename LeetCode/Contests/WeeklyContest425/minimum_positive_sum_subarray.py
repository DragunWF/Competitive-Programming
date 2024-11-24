# https://leetcode.com/contest/weekly-contest-425/problems/minimum-positive-sum-subarray/description/

class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        subs = []
        for i in range(n):
            sub = []
            for j in range(i, n):
                sub.append(nums[j])
                if len(sub) > r:
                    break
                if l <= len(sub) <= r:
                    subs.append([*sub])
        min_sum = -1
        operated = False
        for arr in subs:
            sub_arr_sum = sum(arr)
            if sub_arr_sum > 0 and (not operated or sub_arr_sum < min_sum):
                min_sum = sub_arr_sum
                operated = True
        return min_sum
