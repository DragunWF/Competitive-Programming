// https://www.codewars.com/kata/64fbfe2618692c2018ebbddb

public class CodeWars {
  public static int strCount(String str, char letter) {
    int count = 0;
    char[] input = str.toCharArray();
    for (int i = 0; i < input.length; i++) {
      if (input[i] == letter) count++;
    }
    return count;
  }
}