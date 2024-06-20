// https://www.codewars.com/kata/586560a639c5ab3a260000f3/train/java

import java.util.Arrays; // For testing
import java.util.ArrayList;

public class ScrollingTextMachine {
    public String[] rotate(String text) {
        if (text.isEmpty())
            return new String[0];
        ArrayList<String> rotatedWords = new ArrayList<>();
        for (int i = 0, len = text.length(); i < len; i++) {
            StringBuilder rotated = new StringBuilder();
            for (int j = 0; j < len; j++) {
                rotated.append(
                    text.charAt(i + j >= len ? (i + j) % len : i + j)
                );
            }
            rotatedWords.add(rotated.toString());
        }
        return toArray(rotatedWords);
    }

    public String[] toArray(ArrayList<String> arr) {
        String[] output = new String[arr.size()];
        for (int i = 1; i < output.length; i++) {
            output[i - 1] = arr.get(i);
        }
        output[output.length - 1] = arr.get(0);
        return output;
    }

    public static void main(String[] args) {
        // Not part of the solution, just testing
        // Expected output: ["elloH", "lloHe", "loHel", "oHell", "Hello"]
        System.out.println(Arrays.toString(new ScrollingTextMachine().rotate("Hello")));
    }
}