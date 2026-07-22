// https://leetcode.com/problems/find-target-indices-after-sorting-array/

import java.util.*;

class Solution {
    public List<Integer> targetIndices(int[] nums, int target) {
        List<Integer> output = new ArrayList<>();
        sortArr(nums);
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == target) {
                output.add(i);
            }
        }
        return output;
    }

    private void sortArr(int[] nums) {
        for (int i = 0; i < nums.length - 1; i++) {
            for (int j = 0; j < nums.length - i - 1; j++) {
                if (nums[j] > nums[j + 1]) {
                    int tempNum = nums[j];
                    nums[j] = nums[j + 1];
                    nums[j + 1] = tempNum;
                }
            }
        }
    }

    public static void main(String[] args) {
        // Just testing... Hehe
        Solution solution = new Solution();
        int[] nums = { 1, 2, 5, 2, 3 };
        solution.sortArr(nums);
        for (int num : nums) {
            System.out.println(num);
        }
    }
}