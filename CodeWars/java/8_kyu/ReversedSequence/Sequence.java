// https://www.codewars.com/kata/5a00e05cc374cb34d100000d/train/java

public class Sequence {
    public static int[] reverse(int n) {
        int[] output = new int[n];
        for (int i = 0; i < n; i++) {
            output[i] = n - i;
        }
        return output;
    }
}
