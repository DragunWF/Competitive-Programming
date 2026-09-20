public class CampApexSolution {
    public String countUp(Integer maxLimit) {
        List<Integer> counter = new List<Integer>();
        Integer count = 1;
        while (count <= maxLimit) {
            counter.add(count);
            count++;
        }
        return String.join(counter, ' ');
    }
}