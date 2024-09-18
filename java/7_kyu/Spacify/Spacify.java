// https://www.codewars.com/kata/57f8ee485cae443c4d000127/train/java

public class Spacify {
    public static String spacify(String str) {
        String[] strChars = new String[str.length()];
        for (int i = 0; i < strChars.length; ++i) {
            strChars[i] = String.valueOf(str.charAt(i));
        }
        return String.join(" ", strChars);
    }
}