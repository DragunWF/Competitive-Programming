// https://www.codewars.com/kata/675dc1d3830826975c58a09d/train/java

public class GenerateC {
    public static String generateC(int size) {
        int rowCount = size * 5;
        String[] lines = new String[rowCount];

        for (int i = 0, nth = 1; i < lines.length; i++, nth++) {
            StringBuilder row = new StringBuilder();
            for (int j = 0; j < (nth <= size || nth > lines.length - size ? rowCount : size); j++) {
                row.append("C");
            }
            lines[i] = row.toString();
        }

        return String.join("\n", lines);
    }

    public static void main(String[] args) {
        System.out.println(generateC(1));
        System.out.println(generateC(2));
    }
}