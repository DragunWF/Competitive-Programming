// https://www.codewars.com/kata/57814d79a56c88e3e0000786/train/java

public class Kata {
    public static String encrypt(final String text, final int n) {
        if (text == null)
            return null;
        String initial = text;
        for (int i = 0; i < n; i++) {
            StringBuilder evenIndex = new StringBuilder();
            StringBuilder oddIndex = new StringBuilder();
            for (int j = 0, len = initial.length(); j < len; j++) {
                if (j % 2 == 0) {
                    evenIndex.append(initial.charAt(j));
                } else {
                    oddIndex.append(initial.charAt(j));
                }
            }
            initial = oddIndex.toString() + evenIndex.toString();
        }
        return initial;
    }

    public static String decrypt(final String encryptedText, final int n) {
        if (encryptedText == null)
            return null;
        if (n <= 0)
            return encryptedText;
        int a = (int) Math.ceil(encryptedText.length() / 2.0);
        // System.out.printf("a = %s\n n = %s\n", a, n);
        return encrypt(encryptedText, n <= a ? a - n : n - (n % a));
    }

    public static String testDecrypt(final String text, final int n) {
        if (text == null)
            return null;
        String initial = text;
        for (int i = 0; i < n; i++) {
            StringBuilder evenIndex = new StringBuilder();
            StringBuilder oddIndex = new StringBuilder();
            for (int j = 0, len = initial.length(); j < len; j++) {
                if (j % 2 == 0) {
                    oddIndex.append(initial.charAt(j));
                } else {
                    evenIndex.append(initial.charAt(j));
                }
            }
            initial = oddIndex.toString() + evenIndex.toString();
        }
        return initial;
    }

    public static void main(String[] args) {
        // test code, not part of the solution
        TestCase[] encryptTestCases = {
                new TestCase("This is a test!", 8),
                new TestCase("This kata is very interesting", 15),
                new TestCase("0123456789", 10),
                new TestCase("I do wonder when they're going to be useful.", 41)
        };
        TestCase[] decryptTestCases = {
                new TestCase("hsi  etTi sats!", 5),
                new TestCase("isrtiye iaa iTnteen rvs tkshg", 15),
                new TestCase("This kata is very interesting!", 3),
                new TestCase("I do wonder when they're going to be useful.", 41)
        };

        System.out.println("Encrypt Test Cases:");
        for (int i = 0; i < encryptTestCases.length; i++) {
            TestCase testCase = encryptTestCases[i];
            System.out.printf("Test Case #%s: '%s'\n", i + 1, encrypt(testCase.message, testCase.n));
        }

        System.out.println("\nDecrypt Test Cases:");
        for (int i = 0; i < decryptTestCases.length; i++) {
            TestCase testCase = decryptTestCases[i];
            System.out.printf("Test Case #%s: '%s'\n", i + 1, testDecrypt(testCase.message, testCase.n));
        }
    }
}

class TestCase {
    public String message;
    public int n;

    public TestCase(String message, int n) {
        this.message = message;
        this.n = n;
    }
}