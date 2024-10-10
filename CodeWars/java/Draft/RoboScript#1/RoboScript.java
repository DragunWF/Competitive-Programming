// https://www.codewars.com/kata/58708934a44cfccca60000c4/train/java

public class RoboScript {
    public static String highlight(String code) {
        StringBuilder output = new StringBuilder();
        StringBuilder sequence = new StringBuilder();
        for (int i = 0, n = code.length(); i < n; i++) {
            char c = code.charAt(i);
            if (c == '(' || c == ')') {
                if (!sequence.isEmpty()) {
                    output.append(generateTag(sequence.toString()));
                    sequence = new StringBuilder();
                }
                output.append(c);
                continue;
            }
            if (c == sequence.charAt(0) && !isDigit(c) ||
                    isDigit(sequence.charAt(0)) && isDigit(c)) {
                sequence.append(c);
            } else {
                output.append(generateTag(sequence.toString()));
                sequence = new StringBuilder();
            }
        }
        if (!sequence.isEmpty()) {
            output.append(generateTag(sequence.toString()));
        }
        return output.toString();
    }

    private static String generateTag(String code) {
        char character = code.charAt(0);
        String color;
        switch (character) {
            case 'F':
                color = "pink";
                break;
            case 'L':
                color = "red";
                break;
            case 'R':
                color = "green";
                break;
            default:
                color = "orange";
                break;
        }
        return String.format("<span style=\"color: %s\">%s</span>", color, code);
    }

    private static boolean isDigit(char character) {
        return character >= 48 && character <= 57;
    }

    public static void main(String[] args) {
        // Not part of the solution, just testing
        System.out.println(highlight("FFFR345F2LL"));
        System.out.println();
        System.out.println(highlight("((FR))"));
    }
}