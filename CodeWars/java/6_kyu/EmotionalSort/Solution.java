// https://www.codewars.com/kata/5a86073fb17101e453000258/train/java

import java.util.Arrays;
import java.util.HashMap;

public class Solution {
    public static String[] sortEmotions(boolean order, String[] emotions) {
        HashMap<String, Integer> emotionWeightMap = getEmotionMap();
        int[] emotionWeights = mapEmotionsToWeights(emotions, emotionWeightMap);
        Arrays.sort(emotionWeights);

        String[] sortedEmotions = mapValuesToEmotions(emotionWeights, emotionWeightMap);
        return order ? reverseArray(sortedEmotions) : sortedEmotions;
    }

    private static HashMap<String, Integer> getEmotionMap() {
        HashMap<String, Integer> output = new HashMap<>();
        output.put(":D", 5);
        output.put(":)", 4);
        output.put(":|", 3);
        output.put(":(", 2);
        output.put("T_T", 1);
        return output;
    }

    private static int[] mapEmotionsToWeights(String[] emotions, HashMap<String, Integer> emotionMap) {
        int[] output = new int[emotions.length];
        for (int i = 0; i < output.length; i++) {
            output[i] = emotionMap.get(emotions[i]);
        }
        return output;
    }

    private static String[] reverseArray(String[] arr) {
        String[] reversedArr = new String[arr.length];
        for (int i = arr.length - 1, j = 0; i >= 0; i--, j++) {
            reversedArr[j] = arr[i];
        }
        return reversedArr;
    }

    private static String[] mapValuesToEmotions(int[] emotionWeights, HashMap<String, Integer> emotionMap) {
        String[] output = new String[emotionWeights.length];
        for (int i = 0; i < output.length; i++) {
            for (String key : emotionMap.keySet()) {
                int emotionWeight = emotionMap.get(key);
                if (emotionWeight == emotionWeights[i]) {
                    output[i] = key;
                    break;
                }
            }
        }
        return output;
    }
}