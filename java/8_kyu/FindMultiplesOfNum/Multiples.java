// https://www.codewars.com/kata/58ca658cc0d6401f2700045f/train/java

public class Multiples {
    public static int[] find(int base, int limit) {
        int[] multiples = new int[limit / base];
        for (int i = 0; i < multiples.length; i++) {
            multiples[i] = base * (i + 1);
        }
        return multiples;
    }
}
