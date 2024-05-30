// https://www.codewars.com/kata/59e66e48fc3c499ec5000103/train/java

// For Testing
import java.util.ArrayList;
import java.util.Arrays;

// For the solution
import java.util.List;
import java.util.HashSet;

public class Kata {
    public static int solve(final List<List<Integer>> data) {
        int combos = 1;
        for (int i = 0; i < data.size(); i++)
            combos *= new HashSet<Integer>(data.get(i)).size();
        return combos;
    }

    public static void main(String[] args) {
        // Not part of the actual solution, this is used for testing
        List<List<Integer>> arr = new ArrayList<>();
        arr.add(Arrays.asList(1, 2));
        arr.add(Arrays.asList(4, 4));
        arr.add(Arrays.asList(5, 6, 6));
        System.out.println(solve(arr));
    }
}
