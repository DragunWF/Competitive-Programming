// https://www.codewars.com/kata/55eeddff3f64c954c2000059/train/java

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Consecutives {
    public static List<Integer> sumConsecutives(List<Integer> s) {
        List<Integer> result = new ArrayList<>();
        int currentSum = s.get(0);
        for (int i = 1; i < s.size(); i++) {
            if (s.get(i - 1) == s.get(i)) {
                currentSum += s.get(i);
            } else {
                result.add(currentSum);
                currentSum = s.get(i);
            }
        }
        result.add(currentSum);
        return result;
    }

    public static void main(String[] args) {
        // Not part of the solution, just testing
        // [1,4,4,4,0,4,3,3,1] => [1,12,0,4,6,1]
        System.out.println(Arrays.toString(sumConsecutives(Arrays.asList(1, 4, 4, 4, 0, 4, 3, 3, 1)).toArray()));
    }
}