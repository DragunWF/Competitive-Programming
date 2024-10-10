// https://www.codewars.com/kata/56269eb78ad2e4ced1000013/train/java

public class NumberFun {
    public static long findNextSquare(long sq) {
        if (!isPerfectSquare(sq)) {
            return -1;
        }
        while (!isPerfectSquare(++sq));
        return sq;
    }

    private static boolean isPerfectSquare(long n) {
        return Math.sqrt(n) % 1.0 == 0;
    }

    public static void main(String[] args) {
        // Not part of the solution, just testing
        System.out.println(findNextSquare(121)); // 144
        System.out.println(findNextSquare(625)); // 676
        System.out.println(findNextSquare(114)); // -1
    }
}