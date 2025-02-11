// https://www.codewars.com/kata/565b112d09c1adfdd500019c/train/java

public class SubstringFun {
    public static String nthChar(String[] words) {
        StringBuilder output = new StringBuilder();
        for (int i = 0; i < words.length; i++) {
            output.append(words[i].charAt(i));
        }
        return output.toString();
    }
}