// https://www.codewars.com/kata/525f4206b73515bffb000b21/train/java

import java.util.Collections;
import java.util.Arrays;
import java.util.List;

public class Kata {
    public static String add(String a, String b) {
        // List<Character> arrA = Arrays.asList(a.toCharArray()), arrB =
        // Arrays.asList(b.toCharArray());
        // Collections.reverse(arrA);
        // Collections.reverse(arrB);
        // a = arrA.toString();
        // b = arrB.toString();

        StringBuilder output = new StringBuilder();
        String maxStr = a.length() > b.length() ? a : b;
        boolean carryOne = false;
        for (int i = Math.min(a.length(), b.length()); i >= 0; i--) {
            int sum = Integer.parseInt(String.valueOf(a.charAt(i))) + Integer.parseInt(String.valueOf(b.charAt(i)));
            if (carryOne) {
                sum += 1;
                carryOne = false;
            }
            if (sum >= 10 && i != 0) {
                carryOne = true;
                sum %= 10;
            }
            output.insert(0, sum);
        }
        if (a.length() != b.length()) {
            output.insert(0, maxStr.substring(Math.min(a.length(), b.length())));
        }
        return output.toString();
    }

    public static void main(String[] args) {
        // test code, not part of the solution
        System.out.println(add("123", "321"));
        System.out.println(add("11", "99"));
        System.out.println(add("123", "456"));
        System.out.println(add("888", "222"));
    }
}
