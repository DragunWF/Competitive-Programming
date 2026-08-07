// https://leetcode.com/problems/n-repeated-element-in-size-2n-array/description/

import java.util.HashMap;

class Solution {
    public int repeatedNTimes(int[] nums) {
        HashMap<Integer, Integer> counter = new HashMap<>();
        int n = nums.length / 2;
        for (int num : nums) {
            if (counter.containsKey(num)) {
                int updatedNum = counter.get(num) + 1;
                counter.put(num, updatedNum);
            } else {
                counter.put(num, 1);
            }
        }
        for (int key : counter.keySet()) {
            if (counter.get(key) == n) {
                return key;
            }
        }
        return -1;
    }
}