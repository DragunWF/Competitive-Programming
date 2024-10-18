// https://www.codewars.com/kata/55d410c492e6ed767000004f/train/java

public class Kata {
    private static char[] vowels = { 'a', 'e', 'i', 'o', 'u' };

    public static String vowel2Index(String s) {
        StringBuilder output = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            if (isVowel(s.charAt(i))) {
                output.append(i + 1);
            } else {
                output.append(s.charAt(i));
            }
        }
        return output.toString();
    }

    private static boolean isVowel(char c) {
        for (int i = 0; i < vowels.length; i++) {
            if (c == vowels[i]) {
                return true;
            }
        }
        return false;
    }
}