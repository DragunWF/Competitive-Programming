// https://www.codewars.com/kata/5bc027fccd4ec86c840000b7/train/java

import java.util.List;
import java.util.ArrayList;

public class Solution {
    public static int solve(long n) {
        if (n <= 1)
            return (int) n;
        List<Integer> digitSums = new ArrayList<>();
        long half = n / 2;
        if (n % 2 == 0) {
            digitSums.add(sum(half, half));
            digitSums.add(sum(half - 1, half + 1));
        } else {
            digitSums.add(sum(half, half + 1));
            digitSums.add(sum(half - 1, half));
        }
        return getMax(digitSums);
    }

    private static int sum(long a, long b) {
        return digitSum(a) + digitSum(b);
    }

    private static int digitSum(long n) {
        int sum = 0;
        String strNum = String.valueOf(n);
        for (int i = 0; i < strNum.length(); i++) {
            if (strNum.charAt(i) != '-')
                sum += Integer.parseInt(String.valueOf(strNum.charAt(i)));
        }
        return sum;
    }

    private static int getMax(List<Integer> list) {
        int max = list.get(0);
        for (int i = 1; i < list.size(); i++) {
            if (list.get(i) > max) {
                max = list.get(i);
            }
        }
        return max;
    }

    public static int slowSolve(int n) {
        // Previous attempt
        int max = 0;
        for (int i = 1, j = n - 1; i != j; i++, j--)
            max = Math.max(digitSum(i) + digitSum(j), max);
        return max;
    }

    public static int oldSolve(int n) {
        // Previous attempt
        if (n <= 1)
            return n;
        int half = n / 2;
        List<Integer> digitSums = new ArrayList<>();
        for (int i = 0, j = 1; i < half; i++, j++) {
            int left = digitSum(n % 2 == 0 ? half - j : half - j - 1);
            if (left <= 0)
                break;
            digitSums.add(left + digitSum(half + j));
            System.out.printf("%s + %s = %s\n", left, digitSum(half + j), left + digitSum(half + j));
        }
        if (n % 2 == 0)
            digitSums.add(digitSum(half) + digitSum(half));
        return getMax(digitSums);
    }

    public static void main(String[] args) {
        // Not part of the solution, just testing
        System.out.println(solve(29));
    }
}
