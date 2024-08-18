// https://www.codewars.com/kata/56b29582461215098d00000f/train/java

import java.util.Arrays;

public class Kata {
    public static int[] pipeFix(int[] numbers) {
        int[] range = getMinMax(numbers); // { min, max }
        int[] output = new int[range[1] - range[0] + 1];
        for (int i = 0, n = range[0]; i < output.length; i++, n++) {
            output[i] = n;
        }
        return output;
    }

    private static int[] getMinMax(int[] arr) {
        int min = arr[0], max = arr[0];
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] < min) {
                min = arr[i];
            }
            if (arr[i] > max) {
                max = arr[i];
            }
        }
        return new int[] { min, max };
    }

    public static void main(String[] args) {
        // Not part of the solution, just testing
        int[][] testCases = new int[][] {
                new int[] { 1, 3, 5, 6, 7, 8 },
                new int[] { -1, 6 }
        };
        for (int[] numbers : testCases) {
            System.out.println(Arrays.toString(pipeFix(numbers)));
        }
    }
}