// https://leetcode.com/problems/count-symmetric-integers/

class Solution {
    public int countSymmetricIntegers(int low, int high) {
        int count = 0;
        for (int i = low; i <= high; i++) {
            String strNum = String.valueOf(i);
            if (strNum.length() % 2 != 0) {
                continue;
            }

            int firstHalfSum = 0;
            int secondHalfSum = 0;
            for (int j = 0; j < strNum.length(); j++) {
                int digit = Integer.parseInt(String.valueOf(strNum.charAt(j)));
                if (j < strNum.length() / 2) {
                    firstHalfSum += digit;
                } else {
                    secondHalfSum += digit;
                }
            } 
            if (firstHalfSum == secondHalfSum) {
                count++;
            }
        }
        return count;
    }
}