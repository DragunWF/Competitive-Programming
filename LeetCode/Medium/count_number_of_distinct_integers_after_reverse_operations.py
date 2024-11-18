# https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/description/

class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        initial_len = len(nums)
        distinct = set(nums)
        for i in range(initial_len):
            distinct.add(int(str(nums[i])[::-1]))
        return len(distinct)