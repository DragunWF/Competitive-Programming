// https://www.codewars.com/kata/59cfc000aeb2844d16000075/train/java

import java.util.Arrays;

class Solution {
    public static String[] capitalize(String s) {
        StringBuilder even = new StringBuilder(), odd = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            String letter = String.valueOf(s.charAt(i));
            even.append(i % 2 == 0 ? letter.toLowerCase() : letter.toUpperCase());
            odd.append(i % 2 == 0 ? letter.toUpperCase() : letter.toLowerCase());
        }
        return new String[] { odd.toString(), even.toString() };
    }

    public static void main(String[] args) {
        // Not part of the solution, just testing
        System.out.println(Arrays.toString(capitalize("abcdef")));
    }
}