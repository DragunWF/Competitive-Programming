// https://www.codewars.com/kata/580878d5d27b84b64c000b51/train/java

public class Kata {
    public static int sumTriangularNumbers(int n) {
        int sum = 0;
        for (int i = 0, nth = 1; i < n; i++, nth += 1 + i) {
            sum += nth;
        }
        return sum;
    }

    public static void main(String[] args) {
        // Tests
        System.out.println(sumTriangularNumbers(4));
    }
}