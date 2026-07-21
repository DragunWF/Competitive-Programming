// https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/

class Solution {
    public int maximizeSum(int[] nums, int k) {
        int maxNum = getMaxNum(nums);
        int maxSum = maxNum;
        for (int i = 1; i < k; i++) {
            maxNum++;
            maxSum += maxNum;
        }
        return maxSum;
    }

    private int getMaxNum(int[] nums) {
        int maxNum = nums[0];
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] > maxNum) {
                maxNum = nums[i];
            }
        }
        return maxNum;
    }
}