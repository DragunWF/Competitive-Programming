// https://www.codewars.com/kata/525f47c79f2f25a4db000025/train/java

public class Kata {
    public static boolean validPhoneNumber(String p) {
        if (p.length() != 14 || p.charAt(0) != '(' || p.charAt(4) != ')' || p.charAt(9) != '-')
            return false;
        for (int i = 1, n = p.length(); i < n; i++) {
            if (i == 4 || i == 9 || i == 5)
                continue;
            int charPos = p.charAt(i);
            if (!(charPos >= 48 && charPos <= 57))
                return false;
        }
        return true;
    }

    public static void main(String[] args) {
        // test code not included in the solution
        String[] testCases = { "(123) 456-7890", "(1111)555 2345", "(098) 123 4567" };
        for (int i = 0; i < testCases.length; i++) {
            System.out.printf("Test Case #%s: %s\n",
                    i + 1, validPhoneNumber(testCases[i]));
        }
    }
}
