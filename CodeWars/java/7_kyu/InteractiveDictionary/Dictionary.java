// https://www.codewars.com/kata/57a93f93bb9944516d0000c1/train/java

import java.util.HashMap;

public class Dictionary {
    private HashMap<String, String> wordMap;

    public Dictionary() {
        wordMap = new HashMap<>();
    }

    public void newEntry(String key, String value) {
        wordMap.put(key, value);
    }

    public String look(String key) {
        return wordMap.containsKey(key) ? wordMap.get(key) : "Cant find entry for " + key;
    }
}