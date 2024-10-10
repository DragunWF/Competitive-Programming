// https://www.codewars.com/kata/5279f6fe5ab7f447890006a7/train/java

import java.util.Map;
import java.util.HashMap;
import java.util.List;
import java.util.ArrayList;

public class PickPeaks {
    public static Map<String, List<Integer>> getPeaks(int[] arr) {
        Map<String, List<Integer>> output = new HashMap<>();
        output.put("pos", new ArrayList<Integer>());
        output.put("peaks", new ArrayList<Integer>());
        if (isPlateau(arr)) {
            output.get("pos").add(1);
            output.get("peaks").add(arr[1]);
        } else {
            for (int i = 1; i < arr.length - 1; i++) {
                if (arr[i] > arr[i - 1] && arr[i] > arr[i + 1]) {
                    output.get("pos").add(i);
                    output.get("peaks").add(arr[i]);
                }
            }
        }
        return output;
    }

    private static boolean isPlateau(int[] arr) {
        if (arr[0] == arr[arr.length - 1] && arr[0] < arr[1]) {
            for (int i = 1; i < arr.length - 2; i++) {
                if (arr[i] != arr[i + 1]) {
                    return false;
                }
            }
            return true;
        }
        return false;
    }
}