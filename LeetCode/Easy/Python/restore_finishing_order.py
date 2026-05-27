# https://leetcode.com/problems/restore-finishing-order/

from typing import List


class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        output = []
        for element in order:
            if element in friends:
                output.append(element)
        return output
