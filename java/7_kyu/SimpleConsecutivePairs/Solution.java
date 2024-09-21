// https://www.codewars.com/kata/5a3e1319b6486ac96f000049/train/java

class Solution {
    public static int solve(int[] arr) {
        int count = 0;
        for (int i = 1; i < arr.length; i += 2) {
            if (Math.abs(arr[i] - arr[i - 1]) == 1) {
                count++;
            }
        }
        return count;
    }
}