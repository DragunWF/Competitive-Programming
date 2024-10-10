// https://www.codewars.com/kata/56b7f2f3f18876033f000307/train/java

public class Solution {
    public static boolean isAscOrder(int[] arr) {
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] < arr[i - 1]) {
                return false;
            }
        }
        return true;
    }
}
