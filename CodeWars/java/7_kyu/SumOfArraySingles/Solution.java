// https://www.codewars.com/kata/59f11118a5e129e591000134/train/java

import java.util.HashMap;

public class Solution {
    public static int repeats(int[] arr) {
        int sum = 0;
        HashMap<Integer, Integer> counts = new HashMap<>();
        for (int n : arr) {
            counts.put(n, counts.containsKey(n) ? counts.get(n) + 1 : 1);
        }
        for (int n : counts.keySet()) {
            if (counts.get(n) == 1) {
                sum += n;
            }
        }
        return sum;
    }
}
