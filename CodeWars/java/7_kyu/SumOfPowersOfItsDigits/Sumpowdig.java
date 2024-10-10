// https://www.codewars.com/kata/560a4962c0cc5c2a16000068/train/java

import java.util.Arrays; // For testing
import java.util.ArrayList;

class Sumpowdig {
    public static long[] eqSumPowDig(long hmax, int exp) {
        ArrayList<Long> matches = new ArrayList<>();
        for (long i = 2; i <= hmax; i++) {
            long sum = 0;
            String strNum = String.valueOf(i);
            for (int j = 0; j < strNum.length(); j++) {
                sum += (long) Math.pow(strNum.charAt(j) - 48, exp);
            }
            if (sum == i) {
                matches.add(i);
            }
        }

        long[] output = new long[matches.size()];
        for (int i = 0; i < output.length; i++) {
            output[i] = matches.get(i);
        }
        return output;
    }

    public static void main(String[] args) {
        // Not part of the solution, just testing
        int[] testCases = new int[] { 157, 370, 1000 };
        for (int i = 0; i < testCases.length; i++) {
            System.out.printf("Test Case #%s: %s\n",
                    i + 1, Arrays.toString(eqSumPowDig(testCases[i], 3)));
        }
    }
}
