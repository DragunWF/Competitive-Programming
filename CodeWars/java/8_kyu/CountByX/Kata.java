// https://www.codewars.com/kata/5513795bd3fafb56c200049e/train/java

public class Kata {
    public static int[] countBy(int x, int n) {
        int[] multiples = new int[n];
        for (int i = 1; i <= n; i++)
            multiples[i - 1] = x * i;
        return multiples;
    }
}
