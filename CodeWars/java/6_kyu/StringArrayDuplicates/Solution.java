// https://www.codewars.com/kata/59f08f89a5e129c543000069/train/java

import java.util.Arrays;

class Solution {
    public static String[] dup(String[] arr) {
        String[] output = new String[arr.length];
        for (int i = 0; i < arr.length; i++) {
            StringBuilder newWord = new StringBuilder();
            char lastLetter = arr[i].charAt(0);
            newWord.append(lastLetter);
            for (int j = 1; j < arr[i].length(); j++) {
                if (lastLetter != arr[i].charAt(j)) {
                    newWord.append(arr[i].charAt(j));
                    lastLetter = arr[i].charAt(j);
                }
            }
            output[i] = newWord.toString();
        }
        return output;
    }

    public static void main(String[] args) {
        // Not part of the solution, just testing
        System.out.println(Arrays.toString(
                dup(new String[] { "ccooddddddewwwaaaaarrrrsssss", "piccaninny", "hubbubbubboo" })));
    }
}