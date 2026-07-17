# https://leetcode.com/problems/count-indices-with-opposite-parity/description/

class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        output = []
        for i, num in enumerate(nums):
            count = 0
            for j in range(i + 1, len(nums)):
                if num % 2 != nums[j] % 2:
                    count += 1
            output.append(count)
        return output


def test() -> None:
    # Expected: [2, 1, 1, 0]
    print(Solution().countOppositeParity([1, 2, 3, 4]))


if __name__ == "__main__":
    test()
