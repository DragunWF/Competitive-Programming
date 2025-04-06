// https://www.codewars.com/kata/5a995c2aba1bb57f660001fd/train/java

public class Kata {
    public static String[] scrollingText(String text) {
        String[] output = new String[text.length()];
        String rotatedText = text.toUpperCase();
        output[0] = rotatedText;
        for (int i = 1; i < output.length; i++) {
            rotatedText = rotate(rotatedText);
            output[i] = rotatedText;
        }
        return output;
    }

    private static String rotate(String text) {
        StringBuilder output = new StringBuilder();
        for (int i = 1; i < text.length(); i++) {
            output.append(text.charAt(i));
        }
        output.append(text.charAt(0));
        return output.toString();
    }
}