public class CampApexSolution {
    public Integer sumPositiveOnly(List<Integer> numbers) {
        Integer sum = 0;
        for (Integer num : numbers) {
            if (num < 0) {
                continue;
            }
            sum += num;
        }
        return sum;
    }
}