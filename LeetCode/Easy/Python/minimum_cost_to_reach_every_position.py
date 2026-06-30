# https://leetcode.com/problems/minimum-cost-to-reach-every-position/

from typing import List


class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        current_min = cost[0]
        output = []
        for i in range(len(cost)):
            current_min = min(current_min, cost[i])
            output.append(current_min)
        return output


def test() -> None:
    cost = [5, 3, 4, 1, 3, 2]
    # Expected: [5,3,3,1,1,1]
    print(Solution().minCosts(cost))


if __name__ == "__main__":
    test()
