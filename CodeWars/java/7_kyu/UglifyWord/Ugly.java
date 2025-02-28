// https://www.codewars.com/kata/5ce6cf94cb83dc0020da1929/train/java

public class Ugly {
    private static final char[] letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".toCharArray();

    public static String uglifyWord(String str) {
        boolean flag = true;
        StringBuilder output = new StringBuilder();
        for (int i = 0; i < str.length(); i++) {
            if (isContains(str.charAt(i))) {
                String strChar = String.valueOf(str.charAt(i));
                output.append(flag ? strChar.toUpperCase() : strChar.toLowerCase());
                flag = !flag;
            } else {
                flag = true;
                output.append(str.charAt(i));
            }
        }
        return output.toString();
    }

    private static boolean isContains(char target) {
        for (char c : letters) {
            if (c == target) {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        // This method is used for testing, it is not part of the solution!
        System.out.println(uglifyWord("aaa-bbb-ccc")); // "AaA-BbB-CcC"
    }
}
