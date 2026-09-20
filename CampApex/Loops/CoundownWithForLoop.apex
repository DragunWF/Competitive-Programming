public class CampApexSolution {
    public String countdown(Integer start) {
        List<Integer> countdownList = new List<Integer>();
        for (Integer i = start; i >= 1; i--) {
            countdownList.add(i);
        }
        return String.join(countdownList, ',');
    }
}