public class CampApexSolution {
    public Boolean findInMatrix(List<List<Integer>> matrix, Integer target) {
        for (List<Integer> row : matrix) {
            for (Integer cell : row) {
                if (cell == target) {
                    return true;
                }
            }
        }
        return false;
    }
}