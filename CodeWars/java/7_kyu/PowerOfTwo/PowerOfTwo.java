// https://www.codewars.com/kata/534d0a229345375d520006a0/train/java

public class PowerOfTwo {
    public static boolean isPowerOfTwo(long n) {
        if (n == 0)
            return false;
        return ((double) Math.round((Math.log(n) / Math.log(2)) * 10000) / 10000) % 1.0 == 0.0;
    }

    public static void main(String[] args) {
        // Not part of the solution, just testing
        System.out.println(isPowerOfTwo(1024));
        System.out.println(isPowerOfTwo(333));
        System.out.println((double) Math.round((Math.log(333) / Math.log(2)) * 10000) / 10000);
        System.out.println((double) (Math.log(1024) / Math.log(2)));
    }
}