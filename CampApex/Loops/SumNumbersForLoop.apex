public class CampApexSolution {
    public Integer sumToN(Integer n) {
        Integer sum = 0;
        for (Integer i = 1; i <= n; i++) {
            sum += i;
        }
        return sum;
    }
}