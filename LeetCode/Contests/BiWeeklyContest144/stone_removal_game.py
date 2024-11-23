# https://leetcode.com/contest/biweekly-contest-144/problems/stone-removal-game/description/

class Solution:
    def canAliceWin(self, n: int) -> bool:
        stones = 10
        alice_turn = False
        while n >= stones and stones > 0:
            alice_turn = not alice_turn
            n -= stones
            stones -= 1
        return alice_turn