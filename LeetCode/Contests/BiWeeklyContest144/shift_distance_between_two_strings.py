# https://leetcode.com/contest/biweekly-contest-144/problems/shift-distance-between-two-strings/description/

from typing import List


class Solution:
    def shiftDistance(self, s: str, t: str, nextCost: List[int], previousCost: List[int]) -> int:
        calculatedNext = {}
        calculatedPrevious = {}
        n = len(s)
        min_cost = 0
        
        for i in range(n):
            if s[i] != t[i]:
                s_char_idx = ord(s[i]) - 97
                t_char_idx = ord(t[i]) - 97
                nextRangeCost = None
                previousRangeCost = None
                nextKey = f"{s_char_idx} {t_char_idx}"
                previousKey = f"{s_char_idx} {t_char_idx}"

                if nextKey in calculatedNext:
                    nextRangeCost = calculatedNext[nextKey]
                else:
                    nextRangeCost = self.getRangeSum(s_char_idx, t_char_idx, nextCost, False)
                    calculatedNext[nextKey] = nextRangeCost

                if previousKey in calculatedPrevious:
                    previousRangeCost = calculatedPrevious[previousKey]
                else:
                    previousRangeCost = self.getRangeSum(s_char_idx, t_char_idx, previousCost, True)
                    calculatedPrevious[previousKey] = previousRangeCost

                if nextRangeCost is not None and previousRangeCost is not None:
                    min_cost += min(nextRangeCost, previousRangeCost)
                elif nextRangeCost is not None:
                    min_cost += nextRangeCost
                elif previousRangeCost is not None:
                    min_cost += previousRangeCost
        return min_cost

    def getRangeSum(self, idx1: int, idx2: int, cost: List[int], isPrevious: bool) -> int:
        if idx1 == idx2:
            return 0
        
        total = 0
        if not isPrevious: 
            i = idx1
            while i != idx2:
                total += cost[i]
                i += 1
                if i >= 26:  
                    i = 0
        else: 
            i = idx1
            while i != idx2:
                total += cost[i]
                i -= 1
                if i < 0: 
                    i = 25
        return total


if __name__ == "__main__":
    print(Solution().shiftDistance(
        "abab",
        "baba",
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]))
