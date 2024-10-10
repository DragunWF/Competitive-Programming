// https://www.codewars.com/kata/51675d17e0c1bed195000001/train/java

public class LargestFiveDigitNumber {
    public static int solve(final String digits) {
        int max = 0;
        for (int i = 0; i < digits.length(); i++) {
            StringBuilder num = new StringBuilder();
            for (int j = i; j < digits.length() && j < i + 5; j++) {
                num.append(digits.charAt(j));
            }
            int convertedNum = Integer.parseInt(num.toString());
            if (convertedNum > max) {
                max = convertedNum;
            }
        }
        return max;
    }
}