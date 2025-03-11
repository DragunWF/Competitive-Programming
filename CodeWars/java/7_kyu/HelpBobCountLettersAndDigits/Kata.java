// https://www.codewars.com/kata/5738f5ea9545204cec000155/train/java

public class Kata {
    private static char[] digitsLetters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
            .toCharArray();

    public static int countLettersAndDigits(String input) {
        int count = 0;
        for (int i = 0; i < input.length(); i++) {
            if (isDigitOrLetter(input.charAt(i))) {
                count++;
            }
        }
        return count;
    }

    private static boolean isDigitOrLetter(char c) {
        for (int i = 0; i < digitsLetters.length; i++) {
            if (digitsLetters[i] == c) {
                return true;
            }
        }
        return false;
    }
}