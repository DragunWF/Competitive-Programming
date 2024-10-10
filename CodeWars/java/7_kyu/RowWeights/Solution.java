// https://www.codewars.com/kata/5abd66a5ccfd1130b30000a9/train/java

public class Solution {
    public static int[] rowWeights(final int[] weights) {
        int[] output = new int[2];
        for (int i = 0; i < weights.length; i++) {
            output[i % 2] += weights[i];
        }
        return output;
    }
}