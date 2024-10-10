// https://www.codewars.com/kata/558ee8415872565824000007/train/java

public class Divisible {
    public static boolean isDivisible(int... args) {
        for (int i = 1; i < args.length; i++) {
            if (args[0] % args[i] != 0) {
                return false;
            }
        }
        return true;
    }
}