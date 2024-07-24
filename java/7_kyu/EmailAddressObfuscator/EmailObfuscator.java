// https://www.codewars.com/kata/562d8d4c434582007300004e/train/java

public class EmailObfuscator {
    public static String obfuscate(String email) {
        StringBuilder output = new StringBuilder();
        for (char item : email.toCharArray()) {
            switch (item) {
                case '.':
                    output.append(" [dot] ");
                    break;
                case '@':
                    output.append(" [at] ");
                    break;
                default:
                    output.append(item);
            }
        }
        return output.toString();
    }
}