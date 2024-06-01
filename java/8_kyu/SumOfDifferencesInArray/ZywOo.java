// https://www.codewars.com/kata/5b73fe9fb3d9776fbf00009e/train/java

public class ZywOo {
  public static int sumOfDifferences(int[] arr) {
    int sum = 0;
    if (arr.length > 0) {
      reverseSortArr(arr);
      for (int i = 0; i < arr.length - 1; i++) {
        sum += arr[i] - arr[i + 1];
      }
    }
    return sum;
  }

  private static int[] reverseSortArr(int[] arr) {
    for (int i = 0; i < arr.length; i++) {
      for (int j = 0; j < arr.length - 1; j++) {
        if (arr[j] < arr[j + 1]) {
          int temp = arr[j];
          arr[j] = arr[j + 1];
          arr[j + 1] = temp;
        }
      }
    }
    return arr;
  }

  public static void main(String[] args) {
    // For testing, this is not part of the solution
    int[] output = reverseSortArr(new int[] { 2, 3, 1 });
    for (int num : output) {
      System.out.println(num);
    }
  }
}