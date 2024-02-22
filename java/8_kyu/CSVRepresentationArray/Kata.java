// https://www.codewars.com/kata/5a34af40e1ce0eb1f5000036/train/java

public class Kata {
    public static String toCsvText(int[][] array) {
        String output = "";
        for (int i = 0; i < array.length; i++) {
            for (int j = 0; j < array[i].length; j++) {
                output += String.valueOf(array[i][j]);
                if (j + 1 != array[i].length) output += ",";
            }
            if (i + 1 != array.length) output += "\n";
        }
        return output;
    }
}