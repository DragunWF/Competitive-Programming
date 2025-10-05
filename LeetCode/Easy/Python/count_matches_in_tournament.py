# https://leetcode.com/problems/count-of-matches-in-tournament/

class Solution:
    def numberOfMatches(self, n: int) -> int:
        total_matches = 0
        current_teams = n
        while current_teams != 1:
            if current_teams % 2 == 0:
                matches_played = current_teams // 2
                total_matches += matches_played
                current_teams = matches_played
            else:
                matches_played = (current_teams - 1) // 2
                total_matches += matches_played
                current_teams = matches_played + 1
        return total_matches


def test() -> None:
    solution = Solution()
    print(solution.numberOfMatches(7))  # 6
    print(solution.numberOfMatches(14))  # 13


if __name__ == "__main__":
    test()
