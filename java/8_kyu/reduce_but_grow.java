// https://www.codewars.com/kata/57f780909f7e8e3183000078/train/java

public class Kata {
    public static int grow(int[] x) {
        int product = x[0];
        for (int i = 1; i < x.length; i++)
            product *= x[i];
        return product;
    }
}