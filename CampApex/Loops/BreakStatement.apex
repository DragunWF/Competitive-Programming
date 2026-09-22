public class CampApexSolution {
    public Integer findFirstNegative(List<Integer> numbers) {
        Integer output = 0;
        for (Integer num : numbers) {
            if (num < 0) {
                output = num;
                break;
            }
        }
        return output;
    }
}