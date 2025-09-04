# https://leetcode.com/problems/count-asterisks/description/

class Solution:
    def countAsterisks(self, s: str) -> int:
        pairs = s.split("|")
        count = 0
        for i, pair in enumerate(pairs):
            if i % 2 == 0:
                for char in pair:
                    if char == "*":
                        count += 1
        return count


def test() -> None:
    solution = Solution()
    print(solution.countAsterisks("l|*e*et|c**o|*de|"))  # 2
    print(solution.countAsterisks("yo|uar|e**|b|e***au|tifu|l"))  # 5
    print(solution.countAsterisks("|**|*|*|**||***||"))  # 6


if __name__ == "__main__":
    test()
