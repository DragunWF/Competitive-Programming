// https://www.codewars.com/kata/609eee71109f860006c377d1/train/java

public class Kata {
    public static String lastSurvivor(String letters, int[] coords) {
        String output = letters;
        for (int i = 0; i < coords.length; i++) {
            output = remakeString(output, coords[i]);
        }
        return output;
    }

    private static String remakeString(String str, int filterIndex) {
        StringBuilder output = new StringBuilder();
        for (int i = 0; i < str.length(); i++) {
            if (i != filterIndex) {
                output.append(str.charAt(i));
            }
        }
        return output.toString();
    }

    public static void main(String[] args) {
        // Testing
        System.out.println(lastSurvivor("abc", new int[] { 1, 1 }));
    }
}
