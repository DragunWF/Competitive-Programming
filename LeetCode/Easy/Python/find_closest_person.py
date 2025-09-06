# https://leetcode.com/problems/find-closest-person/

class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        person_one_distance = abs(z - x)
        person_two_distance = abs(z - y)
        if person_one_distance == person_two_distance:
            return 0
        return 1 if person_one_distance < person_two_distance else 2
