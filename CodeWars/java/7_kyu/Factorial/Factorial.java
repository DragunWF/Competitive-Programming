// https://www.codewars.com/kata/57a049e253ba33ac5e000212/train/java

public class Factorial {
    public static long factorial(int n) {
        if (n == 0)
            return 1;
        long result = n;
        for (int i = n - 1; i > 1; i--) {
            result *= i;
        }
        return result;
    }
}
