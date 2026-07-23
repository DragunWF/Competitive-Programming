// https://leetcode.com/problems/sorting-the-sentence/

import java.util.HashMap;

class Solution {
    public String sortSentence(String s) {
        String[] words = s.split(" ");
        HashMap<Integer, String> wordOrder = new HashMap<>();
        for (String word : words) {
            String extractedWord = word.substring(0, word.length() - 1);
            int order = Integer.parseInt(String.valueOf(word.charAt(word.length() - 1)));
            wordOrder.put(order, extractedWord);
        }
        
        StringBuilder output = new StringBuilder();
        for (int i = 1; i <= words.length; i++) {
            output.append(wordOrder.get(i));
            if (i != words.length) {
                output.append(" ");
            }
        }
        return output.toString();
    }
}