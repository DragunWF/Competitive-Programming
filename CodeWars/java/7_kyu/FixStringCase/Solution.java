// https://www.codewars.com/kata/5b180e9fedaa564a7000009a/train/java

public class Solution {
    public static String solve(final String str) {
        int caseCog = 0;
        for (char c : str.toCharArray()) {
            String letter = String.valueOf(c);
            if (letter.equals(letter.toLowerCase())) {
                caseCog++;
            } else {
                caseCog--;
            }
        }
        return caseCog >= 0 ? str.toLowerCase() : str.toUpperCase();
    }
}