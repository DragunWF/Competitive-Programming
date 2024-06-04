// https://www.codewars.com/kata/55b051fac50a3292a9000025/train/java

public class Kata {
    public static long filterString(final String value) {
        StringBuilder output = new StringBuilder();
        for (char letter : value.toCharArray()) {
            if (letter >= 48 && letter <= 57) {
                output.append(letter - 48);
            }
        }
        return Integer.parseInt(output.toString());
    }
}