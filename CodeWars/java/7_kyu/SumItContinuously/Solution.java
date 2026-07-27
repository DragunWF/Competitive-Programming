// https://www.codewars.com/kata/59b44d00bf10a439dd00006f/train/java

import java.util.ArrayList;
import java.util.List;

public class Solution {
  public static List<Integer> add(List<Integer> list) {
    List<Integer> output = new ArrayList<>();
    int currentSum = 0;
    for (int num : list) {
        currentSum += num;
        output.add(currentSum);
    }
    return output;
  }
}