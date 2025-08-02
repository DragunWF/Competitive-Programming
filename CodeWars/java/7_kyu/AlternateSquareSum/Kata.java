// https://www.codewars.com/kata/559d7951ce5e0da654000073/train/java

public class Kata {
    public static int alternateSqSum(int[] arr) {
        int sum = 0;
        for (int i = 0, nth = 1; i < arr.length; i++, nth++) {
            int value = arr[i];
            if (nth % 2 == 0) {
                value *= value;
            }
            sum += value;
        }
        return sum;
    }
}