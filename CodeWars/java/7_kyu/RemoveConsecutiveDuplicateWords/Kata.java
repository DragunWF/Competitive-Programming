// https://www.codewars.com/kata/5b39e91ee7a2c103300018b3/train/java

import java.util.ArrayList;

public class Kata {
    public static String removeConsecutiveDuplicates(String s) {
        ArrayList<String> outputSentence = new ArrayList<String>();
        String[] words = s.split(" ");
        outputSentence.add(words[0]);
        for (int i = 1; i < words.length; i++) {
            if (!words[i - 1].equals(words[i])) {
                outputSentence.add(words[i]);
            }
        }
        return String.join(" ", outputSentence);
    }
}