// https://www.codewars.com/kata/56ed20a2c4e5d69155000301/train/java

import java.util.ArrayList;

public class Scale {

    public static String scale(String str, int k, int v) {
        if (str.isEmpty()) {
            return "";
        }

        ArrayList<String> result = new ArrayList<>();
        String[] lines = str.split("\n");
        for (String line : lines) {
            StringBuilder scaledStr = new StringBuilder();
            for (int i = 0; i < line.length(); i++) {
                scaleChar(scaledStr, k, line.charAt(i));
            }
            for (int i = 0; i < v; i++) {
                result.add(scaledStr.toString());
            }
        }
        return String.join("\n", result);
    }

    private static void scaleChar(StringBuilder scaledStr, int k, char c) {
        for (int i = 0; i < k; i++) {
            scaledStr.append(c);
        }
    }

    public static void main(String[] args) {
        String testCase = "abcd\nefgh\nijkl\nmnop";
        System.out.println(scale(testCase, 2, 3));
        System.out.println(scale("", 5, 5));
    }
}