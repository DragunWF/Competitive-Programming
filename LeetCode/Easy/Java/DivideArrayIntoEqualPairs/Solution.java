// https://leetcode.com/problems/divide-array-into-equal-pairs/

import java.util.HashMap;

class Solution {
    public boolean divideArray(int[] nums) {
        HashMap<Integer, Integer> counter = new HashMap<>();
        for (int num : nums) {
            if (counter.containsKey(num)) {
                counter.put(num, counter.get(num) + 1);
            } else {
                counter.put(num, 1);
            }
        }
        for (int count : counter.values()) {
            if (count % 2 != 0) {
                return false;
            }
        }
        return true;
    }
}