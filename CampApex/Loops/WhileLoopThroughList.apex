public class CampApexSolution {
    public Integer sumUntilLimit(List<Integer> numbers, Integer maxLimit) {
        Integer sum = 0;
        Integer i = 0;
        while (i < numbers.size()) {
            Integer updatedSum = sum + numbers[i];
            if (updatedSum > maxLimit) {
                break;
            }
            sum = updatedSum;
            i++;
        }
        return sum;
    }
}