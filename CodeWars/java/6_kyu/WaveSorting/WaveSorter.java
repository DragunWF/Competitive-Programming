// https://www.codewars.com/kata/596f28fd9be8ebe6ec0000c1/train/java

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;

public class WaveSorter {
    public static void waveSort(int[] array) {
        if (array.length <= 1) {
            return;
        }
        ArrayList<Integer> nums = convertToList(array);
        Collections.sort(nums);
        for (int i = 0; i + 1 < nums.size(); i += 2) {
            array[i + 1] = nums.get(i);
            array[i] = nums.get(i + 1);
        }
        if (array.length % 2 != 0) {
            array[array.length - 1] = nums.get(array.length - 1);
        }
    }

    public static void waveSortOld(int[] array) {
        ArrayList<Integer> nums = convertToList(array);
        HashMap<Boolean, ArrayList<Integer>> parities = new HashMap<>();

        Collections.sort(nums);
        parities.put(true, new ArrayList<>());
        parities.put(false, new ArrayList<>());
        for (int i = 0; i < nums.size(); i++) {
            parities.get(nums.get(i) % 2 != 0).add(nums.get(i));
        }

        int parityIndex = 0;
        for (int i = 0; i < array.length; i++) {
            boolean isEven = i % 2 == 0;
            array[i] = parities.get(isEven).get(parityIndex);
            if (!isEven) {
                parityIndex++;
            }
        }
        System.out.println(nums);
        System.out.println(convertToList(array));
    }

    private static ArrayList<Integer> convertToList(int[] array) {
        ArrayList<Integer> output = new ArrayList<>();
        for (int i = 0; i < array.length; i++) {
            output.add(array[i]);
        }   
        return output;
    }

    public static void main(String[] args) {
        // waveSort(new int[]{ 4, 1, 7, 5, 6, 2, 3 });
        waveSort(new int[]{ 1, 2, 34, 4, 5, 5, 5, 65, 6, 65, 5454, 4 });
        waveSort(new int[]{ 1, 1, 7, 3, 18, 11, 23, 21, 35, 33, 38, 37, 38, 38, 40, 40, 43, 41, 46, 43, 46, 46, 48, 46, 51, 51, 54, 52, 56, 54, 65, 58, 81, 68, 95, 85, 97, 96, 99, 97, 100, 100 });
    }
}
