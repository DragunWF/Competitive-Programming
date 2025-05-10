// https://www.codewars.com/kata/5ac95cb05624bac42e000005/train/java

import java.util.*;

public class FrequencyAnalysisWithBuckets {
    public static ArrayList<ArrayList<Integer>> bucketize(final int[] arr) {
        HashMap<Integer, Integer> numMapCount = getNumMapCount(arr);
        ArrayList<ArrayList<Integer>> output = new ArrayList<>();

        output.add(null);
        for (int i = 1; i <= arr.length; i++) {
            ArrayList<Integer> item = new ArrayList<>();
            for (int key : numMapCount.keySet()) {
                int count = numMapCount.get(key);
                if (count == i) {
                    item.add(key);
                }
            }
            Collections.sort(item);
            output.add(item.isEmpty() ? null : item);
        }
        return output;
    }

    private static HashMap<Integer, Integer> getNumMapCount(int[] arr) {
        HashMap<Integer, Integer> numMapCount = new HashMap<>();
        for (int i = 0; i < arr.length; i++) {
            int num = arr[i];
            if (numMapCount.containsKey(num)) {
                int updatedCount = numMapCount.get(num) + 1;
                numMapCount.put(num, updatedCount);
            } else {
                numMapCount.put(num, 1);
            }
        }
        return numMapCount;
    }

    public static void main(String[] args) {
        System.out.println(bucketize(new int[] { 1, 2, 3, 4, 4, 5, 5, 5 }));
        System.out.println(bucketize(new int[] { 20, 40, 60, 80, 100, 20 }));
    }
}