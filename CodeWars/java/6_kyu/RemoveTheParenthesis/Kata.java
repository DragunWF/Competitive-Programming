// https://www.codewars.com/kata/5f7c38eb54307c002a2b8cc8/train/java

public class Kata {
    public static String removeParentheses(final String str) {
        StringBuilder output = new StringBuilder();
        int isInsideParentheses = 0;
        for (char letter : str.toCharArray()) {
            if (letter == '(') {
                isInsideParentheses++;
            } else if (letter == ')') {
                isInsideParentheses--;
                continue;
            }
            if (isInsideParentheses == 0) {
                output.append(letter);
            }
        }
        return output.toString();
    }
}