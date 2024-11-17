# https://leetcode.com/problems/convert-date-to-binary/description/

class Solution:
    def convertDateToBinary(self, date: str) -> str:
        output = []
        for str_num in date.split("-"):
            output.append(bin(int(str_num))[2:])
        return "-".join(output)