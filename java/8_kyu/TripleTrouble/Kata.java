// https://www.codewars.com/kata/5704aea738428f4d30000914/train/java

public class Kata {
    public static String tripleTrouble(String one, String two, String three) {
        StringBuilder output = new StringBuilder();
        for (int i = 0; i < one.length(); i++) {
            output.append(String.format("%s%s%s", one.charAt(i), two.charAt(i), three.charAt(i)));
        }
        return output.toString();
    }
}