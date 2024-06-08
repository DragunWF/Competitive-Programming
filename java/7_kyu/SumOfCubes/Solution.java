// https://www.codewars.com/kata/59a8570b570190d313000037/train/java

import java.math.BigInteger;

public class Solution {
    public static long sumCubes(long n) {
        BigInteger sum = BigInteger.ZERO;
        for (long i = 1; i <= n; i++) {
            sum = sum.add(BigInteger.valueOf(i * i * i));
        }
        return sum.longValue();
    }

    public static void main(String[] args) {
        // Not part of the solution, just testing
        System.out.println(sumCubes(3));
    }
}