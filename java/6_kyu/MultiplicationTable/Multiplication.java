// https://www.codewars.com/kata/534d2f5b5371ecf8d2000a08/train/java

public class Multiplication {
    public static int[][] multiplicationTable(int n) {
        int[][] result = new int[n][n];
        for (int i = 0, j = 1; i < n; i++, j++) {
            for (int x = 0, y = 1; x < n; x++, y++) {
                result[i][x] = y * j;
            }
        }
        return result;
    }
}
