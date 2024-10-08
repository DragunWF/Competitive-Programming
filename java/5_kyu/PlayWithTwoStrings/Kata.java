// https://www.codewars.com/kata/56c30ad8585d9ab99b000c54/train/java

import java.util.HashMap;

class Kata {
    public static String workOnStrings(String a, String b) {
        HashMap<Character, Integer> charCountA = getCharCount(a);
        HashMap<Character, Integer> charCountB = getCharCount(b);
        return swapCase(a, charCountB) + swapCase(b, charCountA);
    }

    private static HashMap<Character, Integer> getCharCount(String str) {
        HashMap<Character, Integer> charCount = new HashMap<>();
        for (char chr : str.toCharArray()) {
            char lower = toLowerChar(chr);
            if (!charCount.containsKey(lower)) {
                charCount.put(lower, 1);
            } else {
                charCount.put(lower, charCount.get(lower) + 1);
            }
        }
        return charCount;
    }

    private static String swapCase(String str, HashMap<Character, Integer> map) {
        StringBuilder output = new StringBuilder();
        for (char chr : str.toCharArray()) {
            if (map.get(toLowerChar(chr)) == null) {
                output.append(chr);
                continue;
            }
            boolean isSwap = map.get(toLowerChar(chr)) % 2 == 1;
            if (isSwap) {
                String strChar = String.valueOf(chr);
                boolean isLower = strChar.toLowerCase().equals(strChar);
                output.append(isLower ? strChar.toUpperCase() : strChar.toLowerCase());
            } else {
                output.append(chr);
            }
        }
        return output.toString();
    }

    private static char toLowerChar(char chr) {
        return String.valueOf(chr).toLowerCase().charAt(0);
    }

    public static void main(String[] args) {
        // Not part of the solution, just testing
        String[][] testCases = {
                { "abc", "cde" }, // abCCde
                { "ab", "aba" }, // aBABA
                { "abab", "bababa" }, // ABABbababa
                { "abcdeFgtrzw", "defgGgfhjkwqe" }
        };
        for (int i = 0; i < testCases.length; i++) {
            System.out.printf("Test Case #%s: %s\n", i + 1,
                    workOnStrings(testCases[i][0], testCases[i][1]));
        }
    }
}