// https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

class Solution {
    public int findNumbers(int[] nums) {
        int count = 0;
        for (int num : nums) {
            int length = String.valueOf(num).length();
            if (length % 2 == 0) {
                count++;
            }
        }
        return count;
    }
}