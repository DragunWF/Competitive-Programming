// https://www.codewars.com/kata/553e8b195b853c6db4000048/train/java

import java.util.ArrayList;

public class Kata {
    public static boolean hasUniqueChars(String str) {
        ArrayList<Character> seen = new ArrayList<>();
        for (int i = 0, n = str.length(); i < n; i++) {
            if (!seen.contains(str.charAt(i))) {
                seen.add(str.charAt(i));
            } else {
                return false;
            }
        }
        return true;
    }
}