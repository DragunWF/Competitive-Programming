// https://www.codewars.com/kata/565f5825379664a26b00007c/train/java

public class Kata {
    public static int[] getSize(int w, int h, int d) {
        return new int[] { 2 * (d * w + d * h + w * h), w * h * d };
    }
}