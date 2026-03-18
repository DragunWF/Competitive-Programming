// https://www.codewars.com/kata/69b58aaee8f1deef7ece7d0e/train/java

public class Solution {
  public static int breachAttempts(int[] hackers, int securityLevel, int increase) {
    int successfulBreaches = 0;
    for (int hacker : hackers) {
        if (hacker > securityLevel) {
            successfulBreaches++;
        } else {
            securityLevel += increase;
        }
    }
    return successfulBreaches;
  }
}