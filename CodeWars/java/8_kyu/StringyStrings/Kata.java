// https://www.codewars.com/kata/563b74ddd19a3ad462000054/train/java

public class Kata {
    public static String stringy(int size) {
        StringBuilder output = new StringBuilder();
        for (int i = 1; i <= size; i++)
            output.append(i % 2);
        return output.toString();
    }
}
