// https://www.codewars.com/kata/5b4070144d7d8bbfe7000001/train/java

import java.util.HashMap;

public class JomoPipi {
    public static String numericals(String s) {
        HashMap<Character, Integer> occurences = new HashMap<>();
        StringBuilder output = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            char item = s.charAt(i);
            if (occurences.containsKey(item)) {
                int updatedCount = occurences.get(item) + 1;
                occurences.put(item, updatedCount);
                output.append(updatedCount);
            } else {
                occurences.put(item, 1);
                output.append(1);
            }
        }
        return output.toString();
    }
}