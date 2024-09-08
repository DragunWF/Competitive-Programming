// https://www.codewars.com/kata/585b1fafe08bae9988000314/train/java

public class Solution {
    public static String explode(String digits) {
        StringBuilder output = new StringBuilder();
        for (char digit : digits.toCharArray()) {
            String strNum = String.valueOf(digit);
            int num = Integer.parseInt(strNum);
            for (int i = 0; i < num; i++) {
                output.append(strNum);
            }
        }
        return output.toString();
    }
}