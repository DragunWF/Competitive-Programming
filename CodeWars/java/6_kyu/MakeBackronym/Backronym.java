// https://www.codewars.com/kata/55805ab490c73741b7000064/train/java

import java.util.Map;
import java.util.ArrayList;

public class Backronym {
    private static Map<String, String> dictionary = Preload.dictionary;

    public static String makeBackronym(String acronym) {
        ArrayList<String> output = new ArrayList<>();
        for (int i = 0; i < acronym.length(); i++) {
            String strChar = String.valueOf(acronym.charAt(i)).toUpperCase();
            output.add(dictionary.get(strChar));
        }
        return String.join(" ", output);
    }
}

// Not part of the solution, this is to just make the compiler happy
class Preload {
    public static Map<String, String> dictionary;
}