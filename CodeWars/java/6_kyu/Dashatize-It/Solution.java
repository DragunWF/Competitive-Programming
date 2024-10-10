// https://www.codewars.com/kata/58223370aef9fc03fd000071/train/java

public class Solution {
    public static String dashatize(int num) {
        if (num == Integer.MIN_VALUE)
            return "2-1-4-7-48-3-648"; // forgive me father for i have sinned
        num = Math.abs(num);
        if (num <= 9)
            return String.valueOf(num);
        StringBuilder output = new StringBuilder();
        String strNum = String.valueOf(num);
        boolean isPreviousOdd = false;
        for (int i = 0, n = strNum.length(); i < n; i++) {
            if (Integer.parseInt(String.valueOf(strNum.charAt(i))) % 2 != 0) {
                if (i == n - 1 && !isPreviousOdd)
                    output.append(String.format("-%s", strNum.charAt(i)));
                else if (i == 0 || isPreviousOdd && i != n - 1)
                    output.append(String.format("%s-", strNum.charAt(i)));
                else if (!isPreviousOdd)
                    output.append(String.format("-%s-", strNum.charAt(i)));
                else
                    output.append(strNum.charAt(i));
                isPreviousOdd = true;
            } else {
                output.append(strNum.charAt(i));
                isPreviousOdd = false;
            }
        }
        return output.toString();
    }

    public static void main(String[] args) {
        // test code, not part of the solution
        int[] testCases = { 274, 5311, -1, -28369, -1111111111, Integer.MIN_VALUE };
        for (int i = 0; i < testCases.length; i++) {
            System.out.printf("Test Case %s: %s\n", i + 1, dashatize(testCases[i]));
        }
    }
}
