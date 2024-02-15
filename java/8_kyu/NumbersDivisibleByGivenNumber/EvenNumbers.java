// https://www.codewars.com/kata/55edaba99da3a9c84000003b

import java.util.ArrayList;

public class EvenNumbers {
    public static int[] divisibleBy(int[] numbers, int divider) {
        ArrayList<Integer> output = new ArrayList<>();
        for (int num : numbers) {
            if (num % divider == 0) {
                output.add(num);
            }
        }
        int[] arr = new int[output.size()];
        for (int i = 0; i < arr.length; i++) {
            arr[i] = output.get(i);
        }
        return arr;
    }
}
