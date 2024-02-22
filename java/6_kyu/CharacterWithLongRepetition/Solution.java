// https://www.codewars.com/kata/586d6cefbcc21eed7a001155/train/java

public class Solution {
    public static Object[] longestRepetition(String s) {
        if (s.length() == 0)
            return new Object[] { "", 0 };
        char chosenChar = s.charAt(0);
        int maxSeq = 1, currentSeq = 1;
        for (int i = 1, n = s.length(); i < n; i++) {
            if (s.charAt(i - 1) == s.charAt(i)) {
                currentSeq++;
                if (currentSeq > maxSeq) {
                    maxSeq = currentSeq;
                    chosenChar = s.charAt(i);
                }
            } else {
                currentSeq = 1;
            }
        }
        return new Object[] { String.valueOf(chosenChar), maxSeq };
    }
}
