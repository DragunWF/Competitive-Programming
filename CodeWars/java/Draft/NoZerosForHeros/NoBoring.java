// https://www.codewars.com/kata/570a6a46455d08ff8d001002/train/java

public class NoBoring {
    public static int noBoringZeros(int n) {
        if (n == 0)
            return 0;
        String str = String.valueOf(n);
        int endIndex = str.charAt(str.length() - 1);
        for (int i = str.length() - 1; i >= 0; i--) {
            if (str.charAt(i) != '0') {
                endIndex = i;
                break;
            }
        }
        return Integer.parseInt(str.substring(0, endIndex - 1));
    }

    public static void main(String[] args) {
        // test code, not part of the solution
        int[] testCases = { 1530, 0, 1030, 240000, 231 };
        for (int i = 0; i < testCases.length; i++) {
            System.out.printf("Test Case #%s: %s\n",
                    i + 1, noBoringZeros(testCases[i]));
        }
    }
}
