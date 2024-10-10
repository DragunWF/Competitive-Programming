// https://www.codewars.com/kata/57f6ad55cca6e045d2000627/train/java

public class Kata {
    public static int[] squareOrSquareRoot(int[] array) {
        int[] output = new int[array.length];
        for (int i = 0; i < array.length; i++) {
            double sqrt = Math.sqrt(array[i]);
            output[i] = sqrt - Math.floor(sqrt) == 0 ? (int) sqrt : array[i] * array[i];
        }
        return output;
    }
}