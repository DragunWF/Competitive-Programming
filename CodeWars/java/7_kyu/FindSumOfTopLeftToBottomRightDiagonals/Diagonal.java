// https://www.codewars.com/kata/5497a3c181dd7291ce000700/train/java

public class Diagonal {
    public static int diagonalSum(final int[][] matrix) {
        int sum = 0;
        for (int i = 0; i < matrix.length; i++) {
            sum += matrix[i][i];
        }
        return sum;
    }
}