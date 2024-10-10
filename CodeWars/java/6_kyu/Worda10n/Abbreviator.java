// https://www.codewars.com/kata/5375f921003bf62192000746/train/java

public class Abbreviator {
    public String abbreviate(String string) {
        StringBuilder output = new StringBuilder();
        int start = 0, end = 0;
        boolean isWord = false;
        for (int i = 0, n = string.length(); i < n; i++) {
            if (isAlphabet(string.charAt(i))) {
                if (!isWord)
                    start = i;
                if (i + 1 == n)
                    output.append(convert(string.substring(start, n)));
                isWord = true;
            } else {
                if (isWord) {
                    end = i;
                    isWord = false;
                    output.append(convert(string.substring(start, end)));
                }
                output.append(string.charAt(i));
            }
        }
        return output.toString();
    }

    private static String convert(String word) {
        if (word.length() < 4)
            return word;
        return String.format("%s%s%s", word.charAt(0),
                word.length() - 2, word.charAt(word.length() - 1));
    }

    private static boolean isAlphabet(char c) {
        return c >= 65 && c <= 90 || c >= 97 && c <= 122;
    }

    public static void main(String[] args) {
        // test code, not part of the solution
        Abbreviator abbr = new Abbreviator();
        String[] test = {
                "internationalization",
                "The elephant-ride was quite fun!",
                "a: mat'monolithic, is"
        };
        for (int i = 0, j = 1; i < test.length; i++, j++) {
            System.out.printf("Test Case %s: %s\n",
                    j, abbr.abbreviate(test[i]));
        }
    }
}
