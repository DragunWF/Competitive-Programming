public class CampApexSolution {
    public Map<String, Integer> mergeMaps(Map<String, Integer> map1, Map<String, Integer> map2) {
        // Merge both maps, with map2 values taking precedence
        map1.putAll(map2);
        return map1;
    }
}