// https://www.codewars.com/kata/57ee99a16c8df7b02d00045f/train/java

import java.util.ArrayList;
import java.util.Arrays;

public class Kata {
    public static int[] flattenAndSort(int[][] array) {
        ArrayList<Integer> list = new ArrayList<>();
        for (int i = 0; i < array.length; i++) {
            for (int j = 0; j < array[i].length; j++) {
                list.add(array[i][j]);
            }
        }
        int[] output = new int[list.size()];
        for (int i = 0; i < output.length; i++) {
            output[i] = list.get(i);
        }
        Arrays.sort(output);
        return output;
    }
}
