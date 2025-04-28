// https://www.codewars.com/kata/57fcaed83206fb15fd00027a/train/java

public class Kata {
    public static String replaceNth(String text, int n, char oldValue, char newValue) {
        if (n <= 0) {
            return text;
        }

        StringBuilder output = new StringBuilder();
        int occurences = 0;
        for (int i = 0; i < text.length(); i++) {
            char character = text.charAt(i);
            if (character == oldValue) {
                occurences++;
                if (occurences % n == 0) {
                    output.append(newValue);
                    continue;
                }
            }
            output.append(character);
        }
        return output.toString();
    }
}