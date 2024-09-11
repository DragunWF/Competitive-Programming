// https://www.codewars.com/kata/57d2807295497e652b000139/train/java

public class Kata {
    public static double[] averages(int[] numbers) {
        if (numbers == null || numbers.length <= 1)
            return new double[0];
        double[] averages = new double[numbers.length - 1];
        for (int i = 0; i < averages.length; i++) {
            averages[i] = (numbers[i] + numbers[i + 1]) / 2.0;
        }
        return averages;
    }
}