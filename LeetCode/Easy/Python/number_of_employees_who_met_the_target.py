# https://leetcode.com/problems/number-of-employees-who-met-the-target/

from typing import List


class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        return len([hour for hour in hours if hour >= target])


def test() -> None:
    hours = [0, 1, 2, 3, 4]
    target = 2
    print(Solution().numberOfEmployeesWhoMetTarget(hours, target))


if __name__ == "__main__":
    test()
