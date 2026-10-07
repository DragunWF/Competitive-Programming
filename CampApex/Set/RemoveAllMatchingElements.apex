public class CampApexSolution {
    public Set<Integer> removeAllMatching(Set<Integer> originalSet, List<Integer> elementsToRemove) {
        originalSet.removeAll(elementsToRemove);
        return originalSet;
    }
}