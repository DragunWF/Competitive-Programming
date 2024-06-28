// https://www.codewars.com/kata/545afd0761aa4c3055001386/train/java

public class ZywOo {
  public static int[] take(int[] arr, int n) {
    if (n == 0)
      return new int[0];
    if (n > arr.length)
      return arr;
    int[] output = new int[n];
    for (int i = 0; i < n; i++)
      output[i] = arr[i];
    return output;
  }
}
