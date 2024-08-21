// https://www.codewars.com/kata/586bca7fa44cfc833e00005c/train/java

public class Solution {
    public static String[] createArrayOfTiers(int num) {
        String strNum = String.valueOf(num);
        String[] output = new String[strNum.length()];
        for (int i = 0; i < output.length; i++) {
            output[i] = strNum.substring(0, i + 1);
        }
        return output;
    }
}