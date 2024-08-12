// https://www.codewars.com/kata/557e8a141ca1f4caa70000a6/train/java

public class TriangleNumbers {
    public static Boolean isTriangleNumber(long number) {
        for (int total = 1, i = 2; total <= number; total += i, i++) {
            if (total == number)
                return true;
        }
        return false;
    }

    public static void main(String[] args) {
        // Not part of the solution, just testing
        int[] testCases = { 1, 3, 6, 10, 15 };
        // All cases should be true as the output
        for (int number : testCases) {
            System.out.println(isTriangleNumber(number));
        }
    }
}
