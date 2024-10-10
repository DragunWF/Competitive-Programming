// https://www.codewars.com/kata/58daa7617332e59593000006/train/java

public class MostDigits {
    public static int findLongest(int[] numbers) {
        int number = numbers[0];
        int maxDigitLength = getDigitLength(number);
        for (int i = 1; i < numbers.length; i++) {
            int digitLength = getDigitLength(numbers[i]);
            if (digitLength > maxDigitLength) {
                number = numbers[i];
                maxDigitLength = digitLength;
            }
        }
        return number;
    }

    private static int getDigitLength(int number) {
        return String.valueOf(Math.abs(number)).length();
    }
}