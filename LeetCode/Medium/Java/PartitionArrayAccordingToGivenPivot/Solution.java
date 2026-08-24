// https://leetcode.com/problems/partition-array-according-to-given-pivot/

import java.util.ArrayList;

class Solution {
    public int[] pivotArray(int[] nums, int pivot) {
        ArrayList<Integer> firstHalf = new ArrayList<>();
        ArrayList<Integer> secondHalf = new ArrayList<>();
        int pivotCounts = 0;
        for (int num : nums) {
            if (num < pivot) {
                firstHalf.add(num);
            } else if (num > pivot) {
                secondHalf.add(num);
            } else {
                pivotCounts++;
            }
        }

        // Forgive me father for I have sinned
        int[] output = new int[nums.length];
        int counter = 0;
        for (int num : firstHalf) {
            output[counter] = num;
            counter++;
        }
        for (int i = 0; i < pivotCounts; i++) {
            output[counter] = pivot;
            counter++;
        }
        for (int num : secondHalf) {
            output[counter] = num;
            counter++;
        }
        return output;
    }
}