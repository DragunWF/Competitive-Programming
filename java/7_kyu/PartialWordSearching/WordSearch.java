// https://www.codewars.com/kata/54b81566cd7f51408300022d/train/java

import java.util.ArrayList;

class WordSearch {
    static String[] findWord(String x, String[] y) {
        ArrayList<String> words = new ArrayList<>();
        for (int i = 0; i < y.length; i++) {
            if (y[i].toLowerCase().contains(x.toLowerCase())) {
                words.add(y[i]);
            }
        }
        if (words.isEmpty()) {
            return new String[] { "Empty" };
        }
        String[] output = new String[words.size()];
        for (int i = 0; i < output.length; i++) {
            output[i] = words.get(i);
        }
        return output;
    }
}