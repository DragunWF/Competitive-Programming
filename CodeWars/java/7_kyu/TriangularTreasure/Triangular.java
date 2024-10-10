// https://www.codewars.com/kata/525e5a1cb735154b320002c8/train/java

public class Triangular {
    public static long triangular(long n) {
        return n > 0 ? (n * (n + 1)) / 2 : 0;
    }
}