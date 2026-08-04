// https://leetcode.com/problems/a-number-after-a-double-reversal/

class Solution {
    public boolean isSameAfterReversals(int num) {
        StringBuilder reverse1 = new StringBuilder();
        StringBuilder reverse2 = new StringBuilder();

        reverse1.append(String.valueOf(num));
        reverse1.reverse();
        int reversedNum = Integer.parseInt(reverse1.toString());
        reverse2.append(reversedNum);
        reverse2.reverse();
        int finalReversedNum = Integer.parseInt(reverse2.toString());

        return finalReversedNum == num;
    }
}