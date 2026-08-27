// https://leetcode.com/problems/count-valid-prefixes/

class Solution {
    public int countValidPrefixes(String s) {
        int onesCount = 0;
        int zerosCount = 0;
        int validPrefixesCount = 0;
        for (char digit : s.toCharArray()) {
            if (digit == '1') {
                onesCount++;
            } else {
                zerosCount++;
            }
            if (onesCount - 1 == zerosCount || zerosCount - 1 == onesCount || onesCount == zerosCount) {
                validPrefixesCount++;
            }
        }
        return validPrefixesCount;
    }
}