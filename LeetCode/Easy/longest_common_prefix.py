# https://leetcode.com/problems/longest-common-prefix/description/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ""
        min_len = min(len(word) for word in strs)
        for i in range(min_len):
            is_not_common = False
            common = strs[0][i]
            for word in strs:
                if word[i] != common:
                    is_not_common = True
                    break
            if is_not_common:
                break
            output += common
        return output