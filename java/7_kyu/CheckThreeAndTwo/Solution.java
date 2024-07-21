// https://www.codewars.com/kata/5a9e86705ee396d6be000091/train/java

import java.util.HashMap;
import java.util.ArrayList;

public class Solution {
    public boolean checkThreeAndTwo(char[] chars) {
        HashMap<Character, Integer> values = new HashMap<>();
        for (char value : chars) {
            if (!values.containsKey(value)) {
                values.put(value, 1);
            } else {
                values.put(value, values.get(value) + 1);
            }
        }
        if (values.keySet().size() != 2)
            return false;
        Object[] counts = values.values().toArray();
        return (int) counts[0] == 2 && (int) counts[1] == 3 || (int) counts[0] == 3 && (int) counts[1] == 2;
    }
}