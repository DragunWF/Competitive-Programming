// https://www.codewars.com/kata/588a3c3ef0fbc9c8e1000095/train/java

public class Kata {
    public static int maxDiff(int[] lst) {
        if (lst.length <= 1)
            return 0;
        int max = lst[0], min = lst[0];
        for (int i = 1; i < lst.length; i++) {
            if (lst[i] > max) {
                max = lst[i];
            }
            if (lst[i] < min) {
                min = lst[i];
            }
        }
        return max - min;
    }
}