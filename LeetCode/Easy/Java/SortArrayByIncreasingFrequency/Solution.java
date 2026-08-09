// https://leetcode.com/problems/sort-array-by-increasing-frequency/

// Ngl, I was so tired from other stuff today that by the time I did this my logic just felt fuzzy

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;

class Solution {
    public int[] frequencySort(int[] nums) {
        HashMap<Integer, Integer> counter = createCounter(nums);
        int[] output = new int[nums.length];

        ArrayList<Integer> counterKeys = new ArrayList<>(counter.keySet());
        ArrayList<Integer> counterValues = new ArrayList<>(counter.values());
        Collections.sort(counterKeys, Collections.reverseOrder());
        Collections.sort(counterValues);

        boolean[] taken = new boolean[counterKeys.size()];
        int currentOutputIndex = 0;
        for (int value : counterValues) {
            for (int i = 0; i < counterKeys.size(); i++) {
                int key = counterKeys.get(i);
                if (counter.get(key) == value && !taken[i]) {
                    taken[i] = true;
                    for (int j = 0; j < value; j++) {
                        output[currentOutputIndex] = key;
                        currentOutputIndex++;
                    }
                }
            }
        }

        return output;
    }

    private HashMap<Integer, Integer> createCounter(int[] nums) {
        HashMap<Integer, Integer> counter = new HashMap<>();
        for (int num : nums) {
            if (counter.containsKey(num)) {
                int updatedNum = counter.get(num) + 1;
                counter.put(num, updatedNum);
            } else {
                counter.put(num, 1);
            }
        }
        return counter;
    }
}