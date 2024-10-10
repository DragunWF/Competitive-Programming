// https://www.codewars.com/kata/593c9175933500f33400003e/train/java

public class Kata {
    public static int[] multiples(int m, int n) {
        int[] output = new int[m];
        for (int i = 0, j = 1; i < output.length; i++, j++) {
            output[i] = n * j;
        }
        return output;
    }
}