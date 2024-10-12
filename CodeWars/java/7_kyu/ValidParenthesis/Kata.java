// https://www.codewars.com/kata/6411b91a5e71b915d237332d/train/java

import java.util.Stack;

public class Kata {
    public static boolean validParentheses(String parenStr) {
        Stack<Character> opened = new Stack<>();
        for (int i = 0; i < parenStr.length(); i++) {
            char current = parenStr.charAt(i);
            if (current == '(') {
                opened.push(current);
            } else if (current == ')') {
                if (opened.isEmpty())
                    return false;
                opened.pop();
            }
        }
        return opened.isEmpty();
    }
}