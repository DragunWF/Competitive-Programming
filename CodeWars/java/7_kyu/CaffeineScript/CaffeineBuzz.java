// https://www.codewars.com/kata/5434283682b0fdb0420000e6/train/java

public class CaffeineBuzz {
    public static String caffeineBuzz(int n) {
        boolean isJava = n % 3 == 0;
        boolean isCoffee = isJava && n % 4 == 0;

        StringBuilder output = new StringBuilder();
        if (isCoffee) {
            output.append("Coffee");
        } else if (isJava) {
            output.append("Java");
        }
        if (n % 2 == 0 && (isJava || isCoffee)) {
            output.append("Script");
        }

        return output.toString().isEmpty() ? "mocha_missing!" : output.toString();
    }
}