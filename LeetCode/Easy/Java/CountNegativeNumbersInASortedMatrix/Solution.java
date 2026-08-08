// https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/description/

class Solution {
    public int countNegatives(int[][] grid) {
        int count = 0;
        for (int[] row : grid) {
            for (int num : row) {
                if (num < 0) {
                    count++;
                }
            }
        }
        return count;
    }
}