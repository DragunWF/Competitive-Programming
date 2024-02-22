// https://www.codewars.com/kata/58235a167a8cb37e1a0000db/train/java

import java.util.HashMap;

class Kata {
    public static int numberOfPairs(String[] gloves) {
        HashMap<String, Integer> gloveMap = new HashMap<>();
        for (String glove : gloves) {
            gloveMap.put(glove, gloveMap.containsKey(glove) ? gloveMap.get(glove) + 1 : 1);
        }
        int pairs = 0;
        for (String key : gloveMap.keySet()) {
            pairs += gloveMap.get(key) / 2;
        }
        return pairs;
    }
}
