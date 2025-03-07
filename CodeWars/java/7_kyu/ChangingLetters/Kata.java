// https://www.codewars.com/kata/5831c204a31721e2ae000294/train/java

public class Kata {
    private static final String vowels = "aeiou";

    public static String swap(String str) {
        StringBuilder output = new StringBuilder();
        for (char c : str.toCharArray()) {
            String strChar = String.valueOf(c);
            output.append(vowels.contains(strChar) ? strChar.toUpperCase() : strChar);
        }
        return output.toString();
    }
}