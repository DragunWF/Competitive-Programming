// https://www.codewars.com/kata/544a54fd18b8e06d240005c0/train/java

public class Arrays {
    public static int findSmallest(final int[] numbers, final String toReturn) {
        int minIndex = 0;
        int minValue = numbers[minIndex];
        for (int i = 1; i < numbers.length; i++) {
            if (numbers[i] < minValue) {
                minValue = numbers[i];
                minIndex = i;
            }
        }
        return toReturn == "index" ? minIndex : minValue;
    }
}