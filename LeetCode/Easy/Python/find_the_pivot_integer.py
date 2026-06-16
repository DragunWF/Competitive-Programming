# https://leetcode.com/problems/find-the-pivot-integer/

class Solution:
    def pivotInteger(self, n: int) -> int:
        for i, pivot in enumerate(range(1, n + 1)):
            first_half = 0
            second_half = 0
            is_pivot_reached = False
            for j, num in enumerate(range(1, n + 1)):
                if not is_pivot_reached:
                    first_half += num
                    if i == j:
                        is_pivot_reached = True
                        second_half += num
                else:
                    second_half += num
            if first_half == second_half:
                return pivot
        return -1


def test() -> None:
    # Expected: 6
    print(Solution().pivotInteger(8))


if __name__ == "__main__":
    test()
