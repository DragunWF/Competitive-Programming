public class CampApexSolution {
    public Integer sumEvenNumbers(Integer n) {
        Integer sum = 0;
        for (Integer i = 2; i <= n; i += 2) {
            sum += i;
        }
        return sum;
    }
}