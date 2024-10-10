// https://www.codewars.com/kata/58b8c94b7df3f116eb00005b/train/java

public class Kata {
    public static String reverseLetter(final String str) {
        StringBuilder output = new StringBuilder();
        for (int i = str.length() - 1; i >= 0; i--) {
            char c = str.charAt(i);
            if (c >= 65 && c <= 90 || c >= 97 && c <= 122) {
                output.append(c);
            }
        }
        return output.toString();
    }
}