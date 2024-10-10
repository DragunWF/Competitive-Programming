// https://www.codewars.com/kata/54a91a4883a7de5d7800009c/train/java

import java.math.BigInteger;

public class Kata {
    public static String incrementString(String str) {
        if (str.isEmpty() || !isDigit(str.charAt(str.length() - 1))) {
            return str + "1";
        }

        String endingNum = getNumbers(str);
        String word = str.substring(0, str.length() - endingNum.length());
        StringBuilder numStr = new StringBuilder();
        int leadingZeros = 0;
        boolean leading = false;
        for (int i = 0; i < endingNum.length(); i++) {
            char item = endingNum.charAt(i);
            if (item == '0' && !leading && leadingZeros == 0 && i == 0) {
                leading = true;
            } else if (item != '0') {
                leading = false;
            }
            if (leading && i != endingNum.length() - 1) {
                leadingZeros++;
            } else {
                numStr.append(item);
            }
        }

        BigInteger num = new BigInteger(numStr.toString()).add(BigInteger.ONE);
        if (String.valueOf(num).length() > numStr.length()) {
            leadingZeros--;
        }
        StringBuilder zeros = new StringBuilder();
        for (int i = 0; i < leadingZeros; i++) {
            zeros.append('0');
        }
        return word.toString() + zeros.toString() + String.valueOf(num);
    }

    private static String getNumbers(String str) {
        StringBuilder output = new StringBuilder();
        for (int i = str.length() - 1; i >= 0; i--) {
            if (isDigit(str.charAt(i))) {
                output.append(str.charAt(i));
            } else {
                break;
            }
        }
        output.reverse();
        return output.toString();
    }

    private static boolean isDigit(char character) {
        return (character >= '0' && character <= '9');
    }

    private static void mainTest() {
        System.out.println("\nPrimary Test Cases:");
        String[] testCases = {
                "009", "main000", "foo", "foobar23",
                "foo0042", "foo9", "foo099",
                "mcgrUd0000000000278864537079867",
                "<6nl7t/2j2Q00000000000171272734"
        };
        for (String testCase : testCases) {
            System.out.println(incrementString(testCase));
        }
    }

    private static void numbersTest() {
        System.out.println("\nNumbers and Word Test: ");
        String testCase = "<6nl7t/2j2Q00000000000171272734";
        String numStr = getNumbers(testCase);
        String word = testCase.substring(0, testCase.length() - numStr.length());
        System.out.println(numStr);
        System.out.println(word);
    }

    private static void specificTest() {
        System.out.println("Specfic Test:");
        String testCase = "f{?s1OFttF8qmbR$d*GX4:YW?$PR:*$3691278701545310522415250382791";
        String expectedOutput = "f{?s1OFttF8qmbR$d*GX4:YW?$PR:*$3691278701545310522415250382792";
        String actualOutput = incrementString(testCase);
        System.out.printf("Expected: %s\nActual  : %s\nMatch: %s\n",
                expectedOutput, actualOutput, expectedOutput.equals(actualOutput));
    }

    public static void main(String[] args) {
        // Not part of the solution, just testing
        mainTest();
        numbersTest();
        specificTest();
    }
}