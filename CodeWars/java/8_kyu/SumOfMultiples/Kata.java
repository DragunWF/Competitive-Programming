// https://www.codewars.com/kata/57241e0f440cd279b5000829/train/java

public class Kata {
    public static long sumMul(int n, int m) {
        if (n <= 0 || m <= 0)
            throw new IllegalArgumentException();
        long sum = 0;
        for (long i = 1, k = n * i; k < m; i++, k = n * i)
            sum += k;
        return sum;
    }

    public static void main(String[] args) {
        // Test code, not part of the solution
        System.out.println(sumMul(2, 9));
    }
}
