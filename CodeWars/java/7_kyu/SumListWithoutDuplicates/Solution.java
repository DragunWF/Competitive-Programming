// https://www.codewars.com/kata/5993fb6c4f5d9f770c0000f2/train/java

public class Solution {
    public static int sumNoDuplicates(int[] arr) {
        int sum = 0;
        for (int num : arr) {
            if (!isDuplicate(arr, num)) {
                sum += num;
            }
        }
        return sum;
    }

    private static boolean isDuplicate(int[] arr, int n) {
        int count = 0;
        for (int num : arr) {
            if (num == n) {
                count++;
            }
            if (count > 1) {
                return true;
            }
        }
        return false;
    }
}
