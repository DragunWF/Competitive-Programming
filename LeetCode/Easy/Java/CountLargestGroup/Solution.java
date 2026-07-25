// https://leetcode.com/problems/count-largest-group/

import java.util.HashMap;

class Solution {
    public int countLargestGroup(int n) {
        HashMap<Integer, Integer> counter = new HashMap<>();
        for (int i = 1; i <= n; i++) {
            int digitSum = getDigitSum(i);
            if (counter.containsKey(digitSum)) {
                int currentCount = counter.get(digitSum);
                counter.put(digitSum, currentCount + 1);
            } else {
                counter.put(digitSum, 1);
            }
        }
        int maxCount = getMaxValue(counter);
        int largestGroupCount = 0;
        for (int value : counter.values()) {
            if (value == maxCount) {
                largestGroupCount++;
            }
        }
        return largestGroupCount;
    }

    private int getDigitSum(int n) {
        if (n <= 9) {
            return n;
        }
        int total = 0;
        for (char c : String.valueOf(n).toCharArray()) {
            total += Integer.parseInt(String.valueOf(c));
        }
        return total;
    }

    private int getMaxValue(HashMap<Integer, Integer> counter) {
        int maxValue = 0;
        for (int key : counter.keySet()) {
            if (counter.get(key) > maxValue) {
                maxValue = counter.get(key);
            }
        }
        return maxValue;
    }
}