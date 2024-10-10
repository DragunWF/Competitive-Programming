// https://www.codewars.com/kata/57cc975ed542d3148f00015b/train/java

public class Solution {
    public static boolean check(Object[] a, Object x) {
        for (Object item : a) {
            if (item == x) {
                return true;
            }
        }
        return false;
    }
}