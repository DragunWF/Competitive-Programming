// https://www.codewars.com/kata/55ffb44050558fdb200000a4/train/java

public class SumDigNth {

    public static long sumDigNthTerm(long initval, long[] patternl, int nthterm) {
        long output = initval;
        int pattern_idx = 0;
        for (int i = 0; i < nthterm - 1; i++) {
            output += patternl[pattern_idx];
            pattern_idx++;
            if (pattern_idx >= patternl.length) {
                pattern_idx = 0;
            }
        }
        return getDigitSum(output);
    }

    private static long getDigitSum(long num) {
        String strNum = String.valueOf(num);
        long sum = 0;
        for (int i = 0; i < strNum.length(); i++) {
            long digitNum = Long.parseLong(String.valueOf(strNum.charAt(i)));
            sum += digitNum;
        }
        return sum;
    }

    public static void main(String[] args) {
        // Just testing, not part of the solution
        long[] input = { 2, 1, 3 };
        System.out.println(sumDigNthTerm(10, input, 6));
    }
}