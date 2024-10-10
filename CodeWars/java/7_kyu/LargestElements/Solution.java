// https://www.codewars.com/kata/53d32bea2f2a21f666000256/train/java

public class Solution {
    public static int[] largest(int n, int[] arr) {
        int[] output = new int[n];
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr.length - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
        for (int i = arr.length - n, j = 0; i < arr.length; i++, j++) {
            output[j] = arr[i];
        }
        return output;
    }
}