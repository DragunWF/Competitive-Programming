public class CampApexSolution {
    public Integer doWhileDemo(Integer n) {
        Integer sum = 0;
        Integer currentNum = 1;
        do {
            sum += currentNum;
            currentNum++;
        } while (sum <= n);
        return sum;
    }
}