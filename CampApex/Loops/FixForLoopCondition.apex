public class CampApexSolution {
    public String reverseString(String input) {
        String result = '';
        // Bug: Loop condition should start from end
        for (Integer i = input.length() - 1; i >= 0; i--) {
            result += input.substring(i, i + 1);
        }
        return result;
    }
}