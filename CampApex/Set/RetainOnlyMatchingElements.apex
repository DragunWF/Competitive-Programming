public class CampApexSolution {
    public Set<String> retainMatching(Set<String> originalSet, Set<String> elementsToRetain) {
        originalSet.retainAll(elementsToRetain);
        return originalSet;
    }
}