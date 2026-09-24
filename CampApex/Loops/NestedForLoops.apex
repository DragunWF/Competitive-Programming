// Constraints: do not do row * col
// Note: I'd do row * col but the challenge specifically stated that we're suppose to think of an alternative way so I did this instead hehe

public class CampApexSolution {
    public Integer multiplicationValue(Integer row, Integer col) {
        Integer output = 0;
        for (Integer i = 0; i < row; i++) {
            output += col;
        }
        return output;
    }
}