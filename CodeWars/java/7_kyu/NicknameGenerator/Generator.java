// https://www.codewars.com/kata/593b1909e68ff627c9000186/train/java

class Generator {
    private static char[] vowels = "AaEeIiOoUu".toCharArray();

    public static String nickname(String name) {
        if (name.length() < 4)
            return "Error: Name too short";
        return isVowel(name.charAt(2)) ? name.substring(0, 4) : name.substring(0, 3);
    }

    private static boolean isVowel(char ch) {
        for (int i = 0; i < vowels.length; i++) {
            if (vowels[i] == ch) {
                return true;
            }
        }
        return false;
    }
}