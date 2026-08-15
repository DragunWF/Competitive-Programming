// https://leetcode.com/problems/first-letter-to-appear-twice/

import java.util.ArrayList;

class Solution {
    public char repeatedCharacter(String s) {
        ArrayList<Character> seen = new ArrayList<>();
        for (int i = 0; i < s.length(); i++) {
            char currentChar = s.charAt(i);
            if (seen.contains(currentChar)) {
                return currentChar;
            } else {
                seen.add(currentChar);
            }
        }
        return '-';
    }
}