// https://www.codewars.com/kata/57f759bb664021a30300007d/train/java

public class Switch {
    public static String switcheroo(String x) {
        StringBuilder output = new StringBuilder();
        for (char c : x.toCharArray()) {
            if (c != 'a' && c != 'b') {
                output.append(c);
                continue;
            }
            output.append(c == 'a' ? 'b' : 'a');
        }
        return output.toString();
    }
}
