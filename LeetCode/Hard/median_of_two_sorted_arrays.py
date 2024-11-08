# https://leetcode.com/problems/median-of-two-sorted-arrays/description/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sorted_arr = sorted([*nums1, *nums2])
        middle = len(sorted_arr) // 2
        if len(sorted_arr) % 2 == 0:
            return (sorted_arr[middle] + sorted_arr[middle - 1]) / 2
        return sorted_arr[middle]