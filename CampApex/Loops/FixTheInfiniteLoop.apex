public class CampApexSolution {
    public Integer countDigits(Integer num) {
        Integer count = 0;
        while (num > 0) {
            count++;
            num /= 10;
        }
        return count;
    }
}