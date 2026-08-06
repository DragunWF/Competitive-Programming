// https://leetcode.com/problems/remove-trailing-zeros-from-a-string/

class Solution {
    public String removeTrailingZeros(String num) {
        StringBuilder output = new StringBuilder();
        String strNum = String.valueOf(num);
        boolean firstNonZeroFound = false;
        for (int i = num.length() - 1; i >= 0; i--) {
            if (strNum.charAt(i) != '0') {
                firstNonZeroFound = true;
            }
            if (firstNonZeroFound) {
                output.append(strNum.charAt(i));
            }
        }
        output.reverse();
        return output.toString();
    }
}