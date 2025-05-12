// https://leetcode.com/problems/majority-element/description/

import java.util.HashMap;

class Solution {
    public int majorityElement(int[] nums) {
        HashMap<Integer, Integer> counter = countElements(nums);
        int majorityElement = 0;
        int maxCount = 0;
        for (int key : counter.keySet()) {
            if (counter.get(key) > maxCount) {
                majorityElement = key;
                maxCount = counter.get(key);
            }
        }
        return majorityElement;
    }

    private HashMap<Integer, Integer> countElements(int[] nums) {
        HashMap<Integer, Integer> counter = new HashMap<>();
        for (int num : nums) {
            if (!counter.containsKey(num)) {
                counter.put(num, 1);
            } else {
                int updatedCount = counter.get(num) + 1;
                counter.put(num, updatedCount);
            }
        }
        return counter;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.majorityElement(new int[] { 3, 2, 3 }));
        System.out.println(solution.majorityElement(new int[] { 2, 2, 1, 1, 1, 2, 2 }));
    }
}