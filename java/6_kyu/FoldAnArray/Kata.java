// https://www.codewars.com/kata/57ea70aa5500adfe8a000110

import java.util.Scanner;

public class Kata {
    public static int[] foldArray(int[] array, int runs) {
        if (array.length == 1) {
            return array;
        }
        boolean isEvenLength = array.length % 2 == 0;
        int half = array.length / 2 - (isEvenLength ? 1 : 0);
        System.out.println(half);
        int[] output = new int[array.length - half - (isEvenLength ? 1 : 0)];
        for (int i = 0; i <= half; i++) {
            System.out.printf("%s %s\n", i, half);
            int last = array.length - i - 1; // = 3
            if (isEvenLength) {
                output[i] = last >= half ? array[i] + array[last] : array[i];
            } else {
                output[i] = last > half ? array[i] + array[last] : array[i];
            }
            output[i] = last > half ? array[i] + array[last] : array[i];
        }
        if (runs > 1) {
            return foldArray(output, runs - 1);
        }
        return output;
    }

    public static void main(String[] args) {
        // Not part of the solution, this is used for testing purposes
        System.out.print("Runs per test case: ");
        Scanner sc = new Scanner(System.in);
        int runs = sc.nextInt();
        int[][] testCases = {
                { 1, 2, 3, 4, 5 },
                { 9, 6 },
                { -9, 9, -8, 8, 66, 23 }
        };
        for (int i = 0; i < testCases.length; i++) {
            System.out.printf(
                    "Test Case %s: %s\n", i + 1,
                    toStringArr(foldArray(testCases[i], runs)));
        }
        sc.close();
    }

    private static String toStringArr(int[] arr) {
        StringBuilder output = new StringBuilder();
        for (int number : arr) {
            output.append(number + " ");
        }
        return output.toString();
    }
}
