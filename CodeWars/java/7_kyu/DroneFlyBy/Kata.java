// https://www.codewars.com/kata/58356a94f8358058f30004b5/train/java

public class Kata {
    public static String flyBy(String lamps, String drone) {
        StringBuilder output = new StringBuilder();
        for (int i = 0; i < lamps.length(); i++) {
            output.append(i < drone.length() ? 'o' : 'x');
        }
        return output.toString();
    }
}