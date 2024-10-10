// https://www.codewars.com/kata/5ba38ba180824a86850000f7/train/java

import java.util.ArrayList;
import java.util.Collections;

class Solution {
    public static int[] solve(int[] arr) {
        ArrayList<Integer> unique = new ArrayList<>();
        for (int i = arr.length - 1; i >= 0; i--) {
            if (!unique.contains(arr[i])) {
                unique.add(arr[i]);
            }
        }
        Collections.reverse(unique);

        int[] output = new int[unique.size()];
        for (int i = output.length - 1; i >= 0; i--) {
            output[i] = unique.get(i);
        }
        return output;
    }
}