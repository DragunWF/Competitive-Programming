// https://www.codewars.com/kata/5226eb40316b56c8d500030f/train/java

import java.util.Arrays;

public class PascalsTriangle {
    public static long[] generate(int level) {
        long[][] triangle = new long[level][];
        int outputLength = 0;
        for (int i = 0, rowLength = 1; i < level; i++, rowLength++) {
            outputLength += rowLength;
            if (rowLength == 1) {
                triangle[i] = new long[] { 1 };
            } else if (rowLength == 2) {
                triangle[i] = new long[] { 1, 1 };
            } else {
                long[] row = new long[rowLength];
                for (int j = 0; j < rowLength; j++) {
                    if (j == 0 || j == rowLength - 1) {
                        row[j] = 1;
                    } else {
                        row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j];
                    }
                }
                triangle[i] = row;
            }
        }

        long[] output = new long[outputLength];
        int i = 0;
        for (long[] row : triangle) {
            for (long num : row) {
                output[i++] = num;
            }
        }
        return output;
    }

    public static void main(String[] args) {
        // Not part of the solution, just testing
        System.out.println(Arrays.toString(generate(4)));
    }
}