// https://leetcode.com/problems/find-lucky-integer-in-an-array/description/

import java.util.HashMap;

class Solution {
    public int findLucky(int[] arr) {
        HashMap<Integer, Integer> counter = new HashMap<>();
        for (int num : arr) {
            if (counter.containsKey(num)) {
                counter.put(num, counter.get(num) + 1);
            } else {
                counter.put(num, 1);
            }
        }
        int luckyNumber = -1;
        for (int num : counter.keySet()) {
            if (num == counter.get(num) && num > luckyNumber) {
                luckyNumber = num;
            }
        }
        return luckyNumber;
    }
}