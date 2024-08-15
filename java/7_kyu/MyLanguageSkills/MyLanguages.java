// https://www.codewars.com/kata/5b16490986b6d336c900007d/train/java

import java.util.List;
import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.Collections;
import java.util.Map;

public class MyLanguages {
    public static List<String> myLanguages(final Map<String, Integer> results) {
        List<String> output = new ArrayList<>();
        PriorityQueue<Integer> scores = new PriorityQueue<>();
        for (String language : results.keySet()) {
            int score = results.get(language);
            if (score >= 60)
                scores.add(score);
        }
        while (!scores.isEmpty()) {
            for (String language : results.keySet()) {
                if (results.get(language) == scores.peek()) {
                    output.add(language);
                }
            }
            scores.poll();
        }
        Collections.reverse(output);
        return output;
    }
}
