// https://www.codewars.com/kata/5b39e3772ae7545f650000fc/train/java

import java.util.ArrayList;

class Solution {
    public static String removeDuplicateWords(String s) {
        ArrayList<String> seen = new ArrayList<>();
        ArrayList<String> output = new ArrayList<>();
        for (String word : s.split(" ")) {
            if (!seen.contains(word)) {
                seen.add(word);
                output.add(word);
            }
        }
        return String.join(" ", output);
    }
}