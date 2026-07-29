// https://leetcode.com/problems/maximum-number-of-words-you-can-type/

class Solution {
    public int canBeTypedWords(String text, String brokenLetters) {
        String[] words = text.split(" ");
        int count = 0;
        for (String word : words) {
            if (!isIncludes(word, brokenLetters)) {
                count++;
            }
        }
        return count;
    }

    private boolean isIncludes(String pool, String disallowed) {
        char[] disallowedArr = disallowed.toCharArray();
        for (char item : pool.toCharArray()) {
            for (char comparison : disallowedArr) {
                if (item == comparison) {
                    return true;
                }
            }
        }
        return false;
    }
}