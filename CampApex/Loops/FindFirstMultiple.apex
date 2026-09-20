public class CampApexSolution {
    public Integer findFirstMultiple(Integer start, Integer divisor) {
        Integer num = start;
        while (Math.mod(num, divisor) != 0) {
            num++;    
        }
        return num;
    }
}