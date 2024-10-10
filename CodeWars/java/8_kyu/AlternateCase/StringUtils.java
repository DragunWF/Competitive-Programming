// https://www.codewars.com/kata/56efc695740d30f963000557/train/java

public class StringUtils {
    public static String toAlternativeString(String string) {
        String output = "";
        String[] characters = string.split("");
        for (String c : characters) {
            output += c.equals(c.toLowerCase()) ? c.toUpperCase() : c.toLowerCase();
        }
        return output;
    }
}
