# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/ 

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = {}
        elements = set()
        k = 0
        for num in nums:
            if not num in count:
                count[num] = 1
            else:
                count[num] += 1
            if count[num] > 2:
                k += 1
            else:
                elements.add(num)
        nums.clear()
        for num in elements:
            for i in range(min(2, count[num])):
                nums.append(num)
        nums.sort()
        return len(nums)