// https://www.codewars.com/kata/5809c661f15835266900010a/train/java

public class Kata {
    public static int[] doubleEveryOther(int[] arr) {
        int[] output = new int[arr.length];
        for (int i = 0, n = 1; i < arr.length; i++, n++) {
            output[i] = n % 2 == 0 ? arr[i] * 2 : arr[i];
        }
        return output;
    }
}