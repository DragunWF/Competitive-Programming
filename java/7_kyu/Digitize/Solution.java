// https://www.codewars.com/kata/5417423f9e2e6c2f040002ae/train/java

public class Solution {
    public static int[] digitize(int n) {
        String strNum = String.valueOf(n);
        int[] output = new int[strNum.length()];
        for (int i = 0; i < output.length; i++) {
            output[i] = ((int) (strNum.charAt(i))) - 48;
        }
        return output;
    }
}