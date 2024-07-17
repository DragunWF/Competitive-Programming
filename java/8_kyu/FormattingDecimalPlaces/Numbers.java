// https://www.codewars.com/kata/5641a03210e973055a00000d/train/java

public class Numbers {
    public static double TwoDecimalPlaces(double number) {
        return Math.round(number * 100) / 100.0;
    }
}