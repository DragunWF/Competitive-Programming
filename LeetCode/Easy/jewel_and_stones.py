# https://leetcode.com/problems/jewels-and-stones/description/

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_count = 0
        for stone in stones:
            if stone in jewels:
                jewel_count += 1
        return jewel_count