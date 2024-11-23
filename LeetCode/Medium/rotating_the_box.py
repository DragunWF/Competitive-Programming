# https://leetcode.com/problems/rotating-the-box/description/?envType=daily-question&envId=2024-11-23

from typing import List

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        moved_matrix = []
        for row in box:
            moved = []
            str_row = "".join(row).split("*")
            moved_rows = ["".join(sorted(part, reverse=True)) for part in str_row]
            for char in [*("*".join(moved_rows))]:
                moved.append(char)
            moved_matrix.append(moved)
        return self.rotate(list(reversed(moved_matrix)))
        
    def rotate(self, box: List[List[str]]) -> List[List[str]]:
        row_len, column_len = len(box), len(box[0])
        rotated = [[None for i in range(row_len)] for i in range(column_len)]
        for i in range(row_len):
            for j in range(column_len):
                rotated[j][i] = box[i][j]
        return rotated