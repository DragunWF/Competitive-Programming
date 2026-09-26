// Constraints: Do not use the join() function

public class CampApexSolution {
    public String concatenateStrings(List<String> words) {
        String output = '';
        for (Integer i = 0; i < words.size(); i++) {
            output += words[i];
            if (i + 1 != words.size()) {
                output += '-';
            }
        }
        return output;
    }
}