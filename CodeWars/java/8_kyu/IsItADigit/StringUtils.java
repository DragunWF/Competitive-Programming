// https://www.codewars.com/kata/567bf4f7ee34510f69000032/train/java

public class StringUtils {
    public static boolean isDigit(String s) {
        return s.length() == 1 && String.valueOf(s.charAt(0)).matches("[0-9]");
    }

    public static void main(String[] args) {
        // Not part of the solution, just testing
        System.out.println(isDigit("a3")); // false
        System.out.println(isDigit("5")); // true
        System.out.println(isDigit("")); // false
    }
}