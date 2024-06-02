// https://www.codewars.com/kata/5340298112fa30e786000688/train/java

import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

public class Kata {
    private static List<int[]> pairs = new ArrayList<>();

    public static int[][] twosDifference(int[] array) {
        Arrays.sort(array);
        for (int i = 0; i < array.length; i++) {
            for (int j = 0; j < array.length; j++) {
                if (i == j)
                    continue;
                if (Math.abs(array[i] - array[j]) == 2 && !isPairExists(array[i], array[j])) {
                    pairs.add(new int[] { array[i], array[j] });
                }
            }
        }
        int[][] output = new int[pairs.size()][];
        for (int i = 0; i < output.length; i++) {
            output[i] = pairs.get(i);
        }
        return output;
    }

    private static boolean isPairExists(int a, int b) {
        for (int[] pair : pairs) {
            System.out.printf("(%s == %s && %s == %s || %s == %s && %s == %s) = %s\n",
                    pair[0], a, pair[1], b, pair[0], b, pair[1], a,
                    pair[0] == a && pair[1] == b || pair[0] == b && pair[1] == a);
            if (pair[0] == a && pair[1] == b || pair[0] == b && pair[1] == a) {
                return true;
            }
        }
        return false;
    }

    private static void printPairs(int[][] arr) {
        // Test code
        for (int i = 0; i < arr.length; i++) {
            System.out.printf("[%s, %s]\n", arr[i][0], arr[i][1]);
        }
    }

    private static void printArr(int[] arr) {
        // Test code #2
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i]);
            if (i != arr.length - 1) {
                System.out.print(", ");
            }
        }
        System.out.println();
    }

    public static void main(String[] args) {
        // Not part of the solution, just testing
        printArr(twosDifference(new int[] { 1, 3, 4, 6 }));
    }
}