// https://www.codewars.com/kata/5948117018e96c934e000196/train/java

import java.util.Arrays;
import java.util.Collections;
import java.util.ArrayList;

public class Math {
    public static int[] Interval(int[] arr, String str) {
        String[] values = str.split(",");
        if (values.length != 2) {
            return new int[0];
        }

        int startNum = extractNum(values[0]);
        int endNum = extractNum(values[1]);
        if (str.startsWith("(")) {
            startNum++;
        }
        if (str.endsWith(")")) {
            endNum--;
        }

        ArrayList<Integer> intervalList = new ArrayList<>();
        for (int num : arr) {
            if (num >= startNum && num <= endNum) {
                intervalList.add(num);
            }
        }
        Collections.sort(intervalList);
        return toArray(intervalList);
    }

    private static int extractNum(String str) {
        StringBuilder strNum = new StringBuilder();
        for (char character : str.toCharArray()) {
            if ((character >= '0' && character <= '9') || character == '-') {
                strNum.append(character);
            }
        }
        return Integer.parseInt(strNum.toString());
    }

    private static int[] toArray(ArrayList<Integer> list) {
        int[] output = new int[list.size()];
        for (int i = 0; i < list.size(); i++) {
            output[i] = list.get(i);
        }
        return output;
    }

    public static void main(String[] args) {
        // This is used for testing
        System.out.println(Arrays.toString(Interval(new int[] { 1, 2, 3, 4, 5 }, "(2,5)")));
        System.out.println(Arrays.toString(
                Interval(new int[] { -2772, -4362, -2897, -3416, -3504, -4902, -4786, -1902, -1102, -565 },
                        "(-3905,-133]")));
    }
}