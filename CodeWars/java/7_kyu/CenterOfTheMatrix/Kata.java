// https://www.codewars.com/kata/54c91b5228ec4c3b5900036e/train/java

public class Kata {
  public static Integer center(int[][] matrix) {
    if (matrix.length == 0) {
        return null;
    }
    int rows = matrix.length;
    int columns = matrix[0].length;
    if (rows % 2 == 0 || columns % 2 == 0) {
        return null;
    }
    return matrix[Math.floorDiv(rows, 2)][Math.floorDiv(columns, 2)];
  }
}