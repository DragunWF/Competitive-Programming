// https://www.codewars.com/kata/559590633066759614000063/train/java

class MinMax {
    public static int[] minMax(int[] arr) {
        int[] output = { arr[0], arr[0] };
        for (int num : arr) {
            if (num < output[0])
                output[0] = num;
            if (num > output[1])
                output[1] = num;
        }
        return output;
    }
}