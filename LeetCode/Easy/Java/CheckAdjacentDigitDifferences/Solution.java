// https://leetcode.com/problems/check-adjacent-digit-differences/description/

class Solution {
    public boolean isAdjacentDiffAtMostTwo(String s) {
        for (int i = 1; i < s.length(); i++) {
            int prevNum = Integer.parseInt(String.valueOf(s.charAt(i - 1)));
            int currentNum = Integer.parseInt(String.valueOf(s.charAt(i)));
            if (Math.abs(currentNum - prevNum) > 2) {
                return false;
            }
        }
        return true;
    }
}