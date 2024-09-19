// https://www.codewars.com/kata/54557d61126a00423b000a45/train/java

public class ReverseLonger {
    public static String shorterReverseLonger(String a, String b) {
        String shorter = a.length() < b.length() ? a : b;
        String longer = shorter == a ? b : a;
        return String.format("%s%s%s", shorter, reverse(longer), shorter);
    }

    private static String reverse(String a) {
        StringBuilder output = new StringBuilder();
        for (int i = a.length() - 1; i >= 0; i--) {
            output.append(a.charAt(i));
        }
        return output.toString();
    }
}
