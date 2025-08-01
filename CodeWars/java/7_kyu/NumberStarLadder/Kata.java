// https://www.codewars.com/kata/5631213916d70a0979000066/train/java

public class Kata {
    public static String pattern(int n) {
        StringBuilder output = new StringBuilder();
        for (int i = 0, j = 1; i < n; i++, j++) {
            output.append(1);
            for (int k = 0; k < i; k++) {
                output.append("*");
            }
            if (i != 0) {
                output.append(j);
            }

            if (i + 1 != n) {
                output.append("\n");
            }
        }
        return output.toString();
    }

    public static void main(String[] args) {
        System.out.println(pattern(3));
    }
}