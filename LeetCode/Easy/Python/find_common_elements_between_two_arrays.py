# https://leetcode.com/problems/find-common-elements-between-two-arrays/description/

from typing import List


class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        commonElements = set(nums1) & set(nums2)
        answer1, answer2 = 0, 0
        for element in commonElements:
            answer1 += nums1.count(element)
            answer2 += nums2.count(element)
        return [answer1, answer2]
