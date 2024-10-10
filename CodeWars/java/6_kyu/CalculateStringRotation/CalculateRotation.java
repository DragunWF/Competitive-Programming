// https://www.codewars.com/kata/5596f6e9529e9ab6fb000014/train/java

public class CalculateRotation {
    static int shiftedDiff(String first, String second) {
        int rotations = 0;
        while (!first.equals(second)) {
            first = rotate(first);
            rotations++;
            if (rotations > first.length())
                return -1;
        }
        return rotations;
    }

    static String rotate(String str) {
        StringBuilder output = new StringBuilder();
        output.append(str.charAt(str.length() - 1));
        for (int i = 1; i < str.length(); i++) {
            output.append(str.charAt(i - 1));
        }
        return output.toString();
    }

    public static void main(String[] args) {
        // Not part of the solution, just testing
        System.out.println(shiftedDiff("coffee", "eecoff"));
        System.out.println(shiftedDiff("hoop", "pooh"));
    }
}
