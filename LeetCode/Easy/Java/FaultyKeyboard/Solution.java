// https://leetcode.com/problems/faulty-keyboard/

class Solution {
    public String finalString(String s) {
        StringBuilder output = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            char currentChar = s.charAt(i);
            if (currentChar == 'i') {
                output.reverse();
            } else {
                output.append(currentChar);
            }
        }
        return output.toString();
    }
}