// https://www.codewars.com/kata/5572f7c346eb58ae9c000047/train/java

public class Pattern1 {
    public static String pattern(int n) {
        StringBuilder output = new StringBuilder();
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j < i; j++) {
                output.append(i);
            }
            if (i != n) {
                output.append("\n");
            }
        }
        return output.toString();
    }
}