// https://www.codewars.com/kata/56b1f01c247c01db92000076/train/java

public class Solution {
    public static String doubleChar(String s) {
        String output = "";
        for (int i = 0, n = s.length(); i < n; i++) {
            String letter = String.valueOf(s.charAt(i)); 
            output += letter + letter;
        }
        return output;
    }
}
