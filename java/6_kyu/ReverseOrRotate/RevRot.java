// https://www.codewars.com/kata/56b5afb4ed1f6d5fb0000991/train/java

import java.util.ArrayList;

class RevRot {
    public static String revRot(String str, int sz) {
        if (str.isEmpty() || sz == 0)
            return "";
        ArrayList<String> chunks = new ArrayList<>();
        StringBuilder currentChunk = new StringBuilder();
        int currentSum = 0;
        for (int i = 0, nth = 1; i < str.length(); i++, nth++) {
            currentChunk.append(str.charAt(i));
            currentSum += (int) (str.charAt(i) - 48);
            if (nth % sz == 0) {
                chunks.add(currentSum % 2 == 0 ? reverse(currentChunk.toString()) : rotate(currentChunk.toString()));
                currentChunk = new StringBuilder();
                currentSum = 0;
            }
        }
        return String.join("", chunks);
    }

    private static String reverse(String chunk) {
        StringBuilder output = new StringBuilder();
        for (int i = chunk.length() - 1; i >= 0; i--) {
            output.append(chunk.charAt(i));
        }
        return output.toString();
    }

    private static String rotate(String chunk) {
        StringBuilder output = new StringBuilder();
        for (int i = 1; i < chunk.length() - 1; i++) {
            output.append(chunk.charAt(i));
        }
        output.append(chunk.charAt(chunk.length() - 1));
        output.append(chunk.charAt(0));
        return output.toString();
    }

    public static void main(String[] args) {
        // Not part of the solution, just testing
        System.out.println(rotate("123456"));
        System.out.println(reverse("123456"));
        System.out.println(revRot("123456987654", 6));
    }
}