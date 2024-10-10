// https://www.codewars.com/kata/52945ce49bb38560fe0001d9/train/java

public class PascalsTriangle {
    public static int[][] pascal(int depth) {
        int[][] triangle = new int[depth][];
        for (int i = 0, rowLength = 1; i < depth; i++, rowLength++) {
            if (rowLength == 1) {
                triangle[i] = new int[] { 1 };
            } else if (rowLength == 2) {
                triangle[i] = new int[] { 1, 1 };
            } else {
                int[] row = new int[rowLength];
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
        return triangle;
    }
}