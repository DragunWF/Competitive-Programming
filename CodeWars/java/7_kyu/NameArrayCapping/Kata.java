// https://www.codewars.com/kata/5356ad2cbb858025d800111d/train/java

public class Kata {
    public static String[] capMe(String[] arr) {
        String[] output = new String[arr.length];
        for (int i = 0; i < arr.length; i++) {
            String capital = arr[i].substring(0, 1).toUpperCase();
            String lowercasedHalf = arr[i].substring(1).toLowerCase();
            output[i] = capital + lowercasedHalf;
        }
        return output;
    }
}