# https://leetcode.com/problems/find-the-original-array-of-prefix-xor/

from typing import List


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        output = [pref[0], *(0 for _ in range(len(pref) - 1))]
        for i in range(1, len(pref)):
            output[i] = pref[i] ^ pref[i - 1]
        return output


def test() -> None:
    solution = Solution()
    print(solution.findArray([5, 2, 0, 3, 1]))  # [5,7,2,3,2]


if __name__ == "__main__":
    test()


arr = [5, 7, 2, 3, 2]
current_num = arr[0]
for i in range(1, len(arr)):
    current_num ^= arr[i]
print(current_num)
