// https://www.codewars.com/kata/586f6741c66d18c22800010a/train/java

public class Kata {
    public static int sequenceSum(int start, int end, int step) {
        int sum = 0;
        for (int i = start; i <= end; i += step) {
            sum += i;
        }
        return sum;
    }
}
