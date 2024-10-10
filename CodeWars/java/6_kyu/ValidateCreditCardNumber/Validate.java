// https://www.codewars.com/kata/5418a1dd6d8216e18a0012b2/train/java

public class Validate {
    public static boolean validate(String n) {
        int[] result = new int[n.length()];
        int sum = 0;
        for (int i = result.length - 1, j = 1; i >= 0; i--, j++) {
            result[i] = Integer.parseInt(String.valueOf(n.charAt(i)));
            if (j % 2 == 0)
                result[i] *= 2;
            if (result[i] > 9)
                result[i] -= 9;
            sum += result[i];
        }
        return sum % 10 == 0;
    }

    public static void main(String[] args) {
        // test code, not part of the actual solution
        String[] testCases = { "891", "1714" };
        for (int i = 0, j = 1; i < testCases.length; i++, j++) {
            System.out.printf("Test Case #%s: %s\n",
                    j, validate(testCases[i]));
        }
    }
}
