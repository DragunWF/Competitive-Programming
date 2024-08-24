// https://www.codewars.com/kata/56582133c932d8239900002e/train/java

import java.util.HashMap;

public class Kata {
    public static int mostFrequentItemCount(int[] arr) {
        HashMap<Integer, Integer> occurences = new HashMap<>();
        for (int i = 0; i < arr.length; i++) {
            if (occurences.containsKey(arr[i])) {
                occurences.put(arr[i], occurences.get(arr[i]) + 1);
            } else {
                occurences.put(arr[i], 1);
            }
        }
        return getMax(occurences);
    }

    private static int getMax(HashMap<Integer, Integer> map) {
        int max = 0;
        for (int key : map.keySet()) {
            if (map.get(key) > max) {
                max = map.get(key);
            }
        }
        return max;
    }
}