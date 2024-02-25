// https://www.codewars.com/kata/5412509bd436bd33920011bc/train/java

public class Maskify {
    public static String maskify(String str) {
        StringBuilder output = new StringBuilder();
        for (int i = 0, n = str.length(); i < n; i++) {
            output.append(i < n - 4 ? "#" : str.charAt(i));
        }
        return output.toString();
    }
}
