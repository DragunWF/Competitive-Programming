// https://www.codewars.com/kata/5a34b80155519e1a00000009/train/java

import java.util.Arrays;
import java.util.ArrayList;

public class ZywOo {
  public static int[] multipleOfIndex(int[] array) {
    ArrayList<Integer> multiples = new ArrayList<>();
    if (array[0] == 0) {
      multiples.add(array[0]);
    }
    for (int i = 1; i < array.length; i++) {
      if ((double) array[i] % i == 0) {
        multiples.add(array[i]);
      }
    }
    int[] output = new int[multiples.size()];
    for (int i = 0, n = multiples.size(); i < n; i++) {
      output[i] = multiples.get(i);
    }
    return output;
  }

  public static void main(String[] args) {
    // Not part of the solution, just testing
    System.out.println(
        Arrays.toString(multipleOfIndex(new int[] { 22, -6, 32, 82, 9, 25 })));
    System.out.println(Arrays.toString(multipleOfIndex(new int[] { 0, 2, 3, 6, 9 })));
  }
}