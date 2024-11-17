# https://leetcode.com/problems/minimum-index-sum-of-two-lists/

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common = []
        for i, word in enumerate(list1):
            if word in list2:
                common.append([word, list2.index(word) + i])
        min_val = min([item[1] for item in common])
        return [item[0] for item in common if item[1] == min_val]        