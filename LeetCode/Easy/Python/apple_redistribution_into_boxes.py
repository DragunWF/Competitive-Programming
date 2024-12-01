# https://leetcode.com/problems/apple-redistribution-into-boxes/description/

from typing import List


class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total_apples = sum(apple)
        total_boxes = len(capacity)
        capacity.sort(reverse=True)
        nth_box = 0
        while total_apples > 0 and nth_box < total_boxes:
            total_apples -= capacity[nth_box]
            nth_box += 1
        return nth_box
