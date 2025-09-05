# https://leetcode.com/problems/count-items-matching-a-rule/description/

from typing import List


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        ruleKeys = {"type": 0, "color": 1, "name": 2}
        count = 0
        for item in items:
            if item[ruleKeys[ruleKey]] == ruleValue:
                count += 1
        return count


def test() -> None:
    solution = Solution()
    # Expected: 1
    print(solution.countMatches([["phone", "blue", "pixel"], [
          "computer", "silver", "lenovo"], ["phone", "gold", "iphone"]], "color", "silver"))


if __name__ == "__main__":
    test()
