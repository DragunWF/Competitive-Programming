// https://www.codewars.com/kata/5808e2006b65bff35500008f/train/java

public class Kata {
    public static String position(char alphabet) {
        return String.format("Position of alphabet: %s", String.valueOf(alphabet - 96));
    }

    public static void main(String[] args) {
        // Not part of the solution, just testing
        System.out.println(position('a'));
    }
}