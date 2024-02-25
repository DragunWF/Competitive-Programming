// https://www.codewars.com/kata/54a91a4883a7de5d7800009c/train/java

import java.util.Arrays;
import java.util.List;

public class Kata {
    private static List<Character> digits = Arrays.asList(
            '0', '1', '2', '3', '4',
            '5', '6', '7', '8', '9');

    public static String incrementString(String str) {
        if (str.length() == 0)
            return "1";
        if (!digits.contains(str.charAt(str.length() - 1)))
            return String.format("%s%s", str, 1);
        StringBuilder output = new StringBuilder();
        StringBuilder num = new StringBuilder();
        for (int i = 0, n = str.length(); i < n; i++) {
            char character = str.charAt(i);
            if (digits.contains(character)) {
                num.append(character);
            } else {
                output.append(character);
            }
        }
        return String.format("%s%s", output.toString(),
                addOne(num.toString()));
    }

    private static String addOne(String value) {
        StringBuilder num = new StringBuilder();
        StringBuilder leadingZerosStr = new StringBuilder();
        boolean leading = value.charAt(0) == '0';
        for (int i = 0, n = value.length(); i < n; i++) {
            if (leading && value.charAt(i) == '0') {
                leadingZerosStr.append(i + 1 != n ? '0' : '1');
            } else {
                num.append(value.charAt(i));
                leading = false;
            }
        }
        if (num.length() > 0) {
            int incremented = Integer.valueOf(num.toString()) + 1;
            if (String.valueOf(incremented).length() > num.toString().length())
                leadingZerosStr.delete(0, 1);
            return String.format("%s%s", leadingZerosStr.toString(),
                    incremented);
        }
        return leadingZerosStr.toString();
    }

    public static void main(String[] args) {
        // Test code, not part of the solution
        String[] testCases = { "", "foo", "foobar23",
                "foobar002", "main000", "main099", "fo99obar100" };
        for (int i = 0; i < testCases.length; i++) {
            System.out.printf("Test Case #%s: %s\n",
                    i + 1, incrementString(testCases[i]));
        }
    }
}
