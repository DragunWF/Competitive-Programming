// https://www.codewars.com/kata/5899dc03bc95b1bf1b0000ad

public class Kata {
    public static int[] invert(int[] array) {
      int[] output = new int[array.length];
      for (int i = 0; i < array.length; i++) {
        if (array[i] == 0) {
          output[i] = 0;
          continue;
        }
        output[i] = array[i] > 0 ? -array[i] : Math.abs(array[i]);
      }
      return output;
    }
  } invert_values {
    
}
