# https://leetcode.com/problems/sort-the-people/description/

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        output = []
        name_map = {}
        for i in range(len(names)):
            name_map[heights[i]] = names[i]
        for height in sorted(heights, reverse=True):
            output.append(name_map[height])
        return output