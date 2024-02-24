// https://www.codewars.com/kata/52f787eb172a8b4ae1000a34/train/java

import java.math.BigInteger;

public class Solution {
    public static int zeros(int n) {
        BigInteger factorial = BigInteger.valueOf(1);
        for (int i = 1; i <= n; i++)
            factorial = factorial.multiply(BigInteger.valueOf(i));
        String num = String.valueOf(factorial);
        int trailingZeros = 0;
        for (int i = num.length() - 1; i >= 0 && num.charAt(i) == '0'; i--)
            trailingZeros++;
        return trailingZeros;
    }

    public static int original(int n) {
        // long data type cannot hold the maximum n test case
        long factorial = 1;
        for (long i = 1; i <= n; i++)
            factorial *= i;
        String num = String.valueOf(factorial);
        int trailingZeros = 0;
        for (int i = num.length() - 1; i >= 0 && num.charAt(i) == '0'; i--)
            trailingZeros++;
        return trailingZeros;
    }

    public static void main(String[] args) {
        // Test code
        System.out.println(zeros(6));
        System.out.println(zeros(12));
        System.out.println(zeros(18));
    }
}
