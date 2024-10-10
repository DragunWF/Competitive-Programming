// https://www.codewars.com/kata/555bfd6f9f9f52680f0000c5/train/java

public class ReverseNumber {
    public static int reverse(int number) {
        StringBuilder output = new StringBuilder();
        if (number < 0)
            output.append('-');
        String strNum = String.valueOf(Math.abs(number));
        for (int i = strNum.length() - 1; i >= 0; i--) {
            output.append(strNum.charAt(i));
        }
        return Integer.parseInt(output.toString());
    }
}
