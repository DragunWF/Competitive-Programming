// https://www.codewars.com/kata/5bbb8887484fcd36fb0020ca/train/java

public class Solution {
    public static int signChange(int[] arr) {
        int changeCount = 0;
        for (int i = 1; i < arr.length; i++) {
            boolean isPreviousNegative = arr[i - 1] < 0;
            if (isPreviousNegative && arr[i] >= 0 || !isPreviousNegative && arr[i] < 0) {
                changeCount++;
            }
        }
        return changeCount;
    }
}