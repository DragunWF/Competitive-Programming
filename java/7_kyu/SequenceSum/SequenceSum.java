// https://www.codewars.com/kata/56e9e4f516bcaa8d4f001763/train/java

public class SequenceSum {
    public static String showSequence(int value) {
        StringBuilder output = new StringBuilder();
        int sum = 0;
        for (int i = 0; i <= value; i++) {
            sum += i;
            output.append(i);
            if (i != value) {
                output.append("+");
            }
        }
        output.append(" = " + sum);
        return output.toString();
    }
}