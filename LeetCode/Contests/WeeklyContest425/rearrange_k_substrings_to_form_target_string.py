from collections import Counter


class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        n = len(s)
        if k == 1:
            return s == t
        s_substrings, t_substrings = self.k_substrings(s, t, n, k)
        return Counter(s_substrings) == Counter(t_substrings)

    def k_substrings(self, s: str, t: str, n: int, k: int) -> str:
        s_sub_str_arr = []
        s_sub_str = ""
        t_sub_str_arr = []
        t_sub_str = ""
        size = n // k
        for i in range(n):
            s_sub_str += s[i]
            t_sub_str += t[i]
            if (i + 1) % size == 0:
                s_sub_str_arr.append(s_sub_str)
                t_sub_str_arr.append(t_sub_str)
                s_sub_str = ""
                t_sub_str = ""
        return s_sub_str_arr, t_sub_str_arr
