// https://www.codewars.com/kata/5bd00c99dbc73908bb00057a/train/java

import java.util.Collections;
import java.util.ArrayList;

public class Solution {
    public static String alphaSeq(String s) {
        ArrayList<String> output = new ArrayList<>();
        ArrayList<Character> characters = getCharList(s.toLowerCase());

        Collections.sort(characters);
        for (char c : characters) {
            StringBuilder item = new StringBuilder();
            if (c == 'a') {
                item.append('A');
            } else {
                item.append(toUpperCase(c));
                for (int i = 0; i < getPosition(c) - 1; i++) {
                    item.append(c);
                }
            }
            output.add(item.toString());
        }

        return String.join(",", output);
    }

    private static ArrayList<Character> getCharList(String s) {
        char[] chars = s.toCharArray();
        ArrayList<Character> result = new ArrayList<>();
        for (char c : chars) {
            result.add(c);
        }
        return result;
    }

    private static char toUpperCase(char c) {
        return (char) (c - 32);
    }

    private static int getPosition(char c) {
        return (int) (c - 'a') + 1;
    }

    public static void main(String[] args) {
        System.out.println(getPosition('a'));
        System.out.println(toUpperCase('a'));
        System.out.println(alphaSeq("zxyabc"));
    }
}