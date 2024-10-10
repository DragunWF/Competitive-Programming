// https://www.codewars.com/kata/5436f26c4e3d6c40e5000282/train/java

import java.util.Arrays; // For testing

public class SequenceSum {
    public static int[] sumOfN(int n) {
        int[] output = new int[Math.abs(n) + 1];
        for (int i = 1, j = 1; i <= Math.abs(n); i++, j++) {
            output[i] = output[i - 1] + (n < 0 ? -j : j);
        }
        return output;
    }

    public static void main(String[] args) {
        // Not part of the solution, just testing
        int[] testCases = new int[] { 3, 5, -5, 7, 10 };
        for (int i = 0; i < testCases.length; i++) {
            System.out.printf("Test Case #%s: %s\n",
                    i + 1, Arrays.toString(sumOfN(testCases[i])));
        }
    }
}
