// https://www.codewars.com/kata/583989556754d6f4c700018e/train/java

import java.util.*;

public class Solution {
    public static List<Integer> findMultiples(int a, int b, int limit) {
        ArrayList<Integer> output = new ArrayList<>();
        for (int num = 1; num <= limit; num++) {
            if (num % a == 0 && num % b == 0) {
                output.add(num);
            }
        }
        return output;
    }
}