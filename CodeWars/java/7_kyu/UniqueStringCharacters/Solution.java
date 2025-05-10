// https://www.codewars.com/kata/5a262cfb8f27f217f700000b/train/java

class Solution {
    public static String solve(String a, String b) {
        StringBuilder unique = new StringBuilder();
        addUnique(unique, a, b);
        addUnique(unique, b, a);
        return unique.toString();
    }

    private static void addUnique(StringBuilder unique, String base, String compare) {
        for (int i = 0; i < base.length(); i++) {
            char currentChar = base.charAt(i);
            if (!contains(compare, currentChar)) {
                unique.append(currentChar);
            }
        }
    }

    private static boolean contains(String str, char compareChar) {
        for (int i = 0; i < str.length(); i++) {
            if (compareChar == str.charAt(i)) {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        System.out.println(solve("xyab", "xzca")); // "ybzc"
    }
}