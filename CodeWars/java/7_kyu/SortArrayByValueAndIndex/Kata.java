// https://www.codewars.com/kata/58e0cb3634a3027180000040/train/java

public class Kata {
    public static int[] sortByValueAndIndex(int[] array) {
        int[] result = new int[array.length];
        for (int i = 0, n = 1; i < array.length; i++, n++) {
            result[i] = array[i] * n;
        }
        for (int i = 0; i < result.length; i++) {
            for (int j = 0; j < array.length - 1; j++) {
                if (result[j] > result[j + 1]) {
                    swap(array, j);
                    swap(result, j);
                }
            }
        }
        return array;
    }

    private static void swap(int[] array, int i) {
        int temp = array[i];
        array[i] = array[i + 1];
        array[i + 1] = temp;
    }
}