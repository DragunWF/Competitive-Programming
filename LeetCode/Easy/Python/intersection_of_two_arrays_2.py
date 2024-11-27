# https://leetcode.com/problems/intersection-of-two-arrays-ii/description/

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        for num in set(nums1):
            if num in nums2:
                min_count = min(nums1.count(num), nums2.count(num))
                for i in range(min_count):
                    output.append(num)
        return output