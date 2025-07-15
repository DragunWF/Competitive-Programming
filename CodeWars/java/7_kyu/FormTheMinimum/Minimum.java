// https://www.codewars.com/kata/5ac6932b2f317b96980000ca/train/java

import java.util.ArrayList;
import java.util.Collections;

public class Minimum {
    public static int minValue(int[] values) {
        ArrayList<Integer> uniqueNumList = convertToUniqueList(values);
        Collections.sort(uniqueNumList);
        StringBuilder minStrNum = new StringBuilder();
        for (int num : uniqueNumList) {
            minStrNum.append(num);
        }
        return Integer.parseInt(minStrNum.toString());
    }

    private static ArrayList<Integer> convertToUniqueList(int[] arr) {
        ArrayList<Integer> output = new ArrayList<>();
        for (int i = 0; i < arr.length; i++) {
            if (output.indexOf(arr[i]) == -1) {
                output.add(arr[i]);
            }
        }
        return output;
    }

    public static void main(String[] args) {
        // For testing
        System.out.println(minValue(new int[] { 1, 3, 1 })); // 13
    }
}