// https://www.codewars.com/kata/54bf85e3d5b56c7a05000cf9/train/java

import java.util.*;

public class LineNumbering {
    public static List<String> number(List<String> lines) {
        List<String> output = new ArrayList<>();
        for (int i = 1, n = lines.size(); i <= n; i++)
            output.add(String.format("%s: %s", i, lines.get(i - 1)));
        return output;
    }

    public static void main(String[] args) {
        // Test code, not included in the solution
        List<String> output = number(Arrays.asList("a", "b", "c"));
        for (String item : output) {
            System.out.println(item);
        }
    }
}
