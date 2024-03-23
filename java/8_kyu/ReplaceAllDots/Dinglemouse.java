// https://www.codewars.com/kata/596c6eb85b0f515834000049/train/java

public class Dinglemouse {
    public static String replaceDots(final String str) {
        StringBuilder output = new StringBuilder();
        for (int i = 0, n = str.length(); i < n; i++) {
            output.append(str.charAt(i) == '.' ? '-' : str.charAt(i));
        }
        return output.toString();
    }
}
