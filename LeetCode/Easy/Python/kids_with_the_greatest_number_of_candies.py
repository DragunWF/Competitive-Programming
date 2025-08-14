# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies

from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        dp = {}
        output = []
        for kidCandyCount in candies:
            updatedCount = kidCandyCount + extraCandies
            if updatedCount in dp:
                output.append(dp[updatedCount])
            else:
                hasGreaterCandies = self.hasGreaterCandiesThanAll(
                    updatedCount, candies)
                dp[updatedCount] = hasGreaterCandies
                output.append(hasGreaterCandies)
        return output

    def hasGreaterCandiesThanAll(self, candyCount: int, candies: List[int]) -> bool:
        return all(candyCount >= kidCandyCount for kidCandyCount in candies)


def test() -> None:
    solution = Solution()
    # [true,true,true,false,true]
    print(solution.kidsWithCandies([2, 3, 5, 1, 3], 3))

    # [true,false,false,false,false]
    print(solution.kidsWithCandies([4, 2, 1, 1, 2], 1))


if __name__ == "__main__":
    test()
