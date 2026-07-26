// https://leetcode.com/problems/matrix-diagonal-sum/description/

class Solution {
    public int diagonalSum(int[][] mat) {
        int start = 0;
        int end = mat.length - 1;
        int sum = 0;
        for (int i = 0; i < mat.length; i++) {
            sum += mat[i][start];
            if (start != end) {
                sum += mat[i][end];
            }
            if (i < mat.length / 2) {
                start++;
                end--;
            } else {
                start--;
                end++;
            }
            if (start > end) {
                start--;
                end++;
            }
        }
        return sum;
    }
}