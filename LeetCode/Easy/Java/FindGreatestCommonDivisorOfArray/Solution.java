// https://leetcode.com/problems/find-greatest-common-divisor-of-array/

class Solution {
    public int findGCD(int[] nums) {
        int maxNum = nums[0];
        int minNum = nums[0];
        for (int num : nums) {
            if (num > maxNum) {
                maxNum = num;
            }
            if (num < minNum) {
                minNum = num;
            }
        }
        return getGcd(maxNum, minNum);
    }

    private int getGcd(int a, int b) {
        return b == 0 ? Math.abs(a) : getGcd(b, a % b);
    }
}