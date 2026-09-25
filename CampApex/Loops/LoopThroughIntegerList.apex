// https://www.campapex.org/practice/loops

public class CampApexSolution {
    public Decimal calculateAverage(List<Integer> numbers) {
        Decimal sum = 0;
        for (Integer num : numbers) {
            sum += num;
        }
        if (sum == 0) {
            return sum;
        }
        return sum / numbers.size();
    }
}