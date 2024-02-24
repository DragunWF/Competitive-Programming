// https://www.codewars.com/kata/5848565e273af816fb000449/train/java

public class Kata {
    public static String encryptThis(String text) {
        if (text.length() == 0)
            return "";
        String[] words = text.split(" ");
        String[] output = new String[words.length];
        for (int i = 0; i < output.length; i++) {
            int asciiPos = (int) words[i].charAt(0);
            if (words[i].length() <= 2) {
                output[i] = String.valueOf(asciiPos);
                if (words[i].length() == 2)
                    output[i] += String.valueOf(words[i].charAt(1));
                continue;
            }
            String secondLetter = String.valueOf(words[i].charAt(1));
            String lastLetter = String.valueOf(words[i].charAt(words[i].length() - 1));
            output[i] = String.format("%s%s%s%s", asciiPos, lastLetter,
                    words[i].substring(2, words[i].length() - 1), secondLetter);
        }
        return String.join(" ", output);
    }

    public static void main(String[] args) {
        // Test code (Not included in the solution)
        System.out.println(encryptThis("Hello"));
        System.out.println(encryptThis("A wise old owl lived in an oak"));
    }
}
