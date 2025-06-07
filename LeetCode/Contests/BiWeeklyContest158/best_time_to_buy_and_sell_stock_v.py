# https://leetcode.com/contest/biweekly-contest-158/problems/best-time-to-buy-and-sell-stock-v/
# Solution Status - Memory Limit Exceeded

from typing import List


class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        N = len(prices)
        seen = {}

        def getProfit(day: int, trans_left: int, state: int) -> int:
            NEUTRAL = 0
            HOLDING = 1

            if day >= N or trans_left == 0:
                return 0 if state == 0 else float("-inf")
            if (day, trans_left, state) in seen:
                return seen[(day, trans_left, state)]

            result = getProfit(day + 1, trans_left, state)
            if state == NEUTRAL:
                result = max(result,
                             getProfit(day + 1, trans_left, 1) - prices[day],
                             getProfit(day + 1, trans_left, -1) + prices[day])
            elif state == HOLDING:
                result = max(result,
                             getProfit(day + 1, trans_left - 1, 0) + prices[day])
            else:  # Short Position State
                result = max(result,
                             getProfit(day + 1, trans_left - 1, 0) - prices[day])

            seen[(day, trans_left, state)] = result
            return result

        return getProfit(0, k, 0)
