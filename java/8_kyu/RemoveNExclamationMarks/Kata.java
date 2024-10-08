// https://www.codewars.com/kata/57faf7275c991027af000679/train/java

public class Kata {
    public static String remove(String s, int n) {
        StringBuilder output = new StringBuilder();
        int marksRemoved = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '!' && marksRemoved < n) {
                marksRemoved++;
            } else {
                output.append(s.charAt(i));
            }
        }
        return output.toString();
    }
}