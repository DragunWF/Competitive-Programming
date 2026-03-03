// https://www.codewars.com/kata/58e0f0bf92d04ccf0a000010/train/java

public class Kata {
  public static int lostSheep(int[] fridayNightCounting, int[] saturdayNightCounting, int sheepTotal) {
    return sheepTotal - (sum(fridayNightCounting) + sum(saturdayNightCounting));
  }

  private static int sum(int[] arr) {
    int total = 0;
    for (int num : arr) {
        total += num;
    }
    return total;
  }
}