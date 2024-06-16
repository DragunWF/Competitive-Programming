// https://www.codewars.com/kata/51689e27fe9a00b126000004/train/java

import java.util.ArrayList;

public class Kata {
    public static String formatWords(String[] words) {
        if (words == null)
            return "";
        ArrayList<String> filteredWords = new ArrayList<>();
        for (String word : words) {
            if (!word.isEmpty()) {
                filteredWords.add(word);
            }
        }
        if (filteredWords.size() == 0)
            return "";
        if (filteredWords.size() == 1)
            return filteredWords.get(0);

        StringBuilder output = new StringBuilder();
        for (int i = 0; i < filteredWords.size(); i++) {
            String word = filteredWords.get(i);
            output.append(word);
            if (i == filteredWords.size() - 2) {
                output.append(" and ");
            } else if (i < filteredWords.size() - 1) {
                output.append(", ");
            }
        }
        return output.toString();
    }

    public static void main(String[] args) {
        // Not part of the solution, just testing
        System.out.println(formatWords(new String[] { "one", "two", "three", "four" }));
    }
}