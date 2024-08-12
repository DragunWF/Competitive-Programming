// https://www.codewars.com/kata/5254bd1357d59fbbe90001ec/train/java

public class Sequence {
    public static long getScore(long n) {
        long output = 0;
        for (long i = 1, prev = 0; i <= n; i++, prev = output) {
            output = 50 * i + prev;
        }
        return output;
    }
}