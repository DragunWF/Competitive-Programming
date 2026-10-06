public class CampApexSolution {
    public Map<String, Integer> countOccurrences(List<String> words) {
        Map<String, Integer> counter = new Map<String, Integer>();
        for (String word : words) {
            if (counter.containsKey(word)) {
                counter.put(word, counter.get(word) + 1);
            } else {
                counter.put(word, 1);
            }
        }
        return counter;
    }
}