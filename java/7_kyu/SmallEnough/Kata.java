// https://www.codewars.com/kata/57cc981a58da9e302a000214/train/java

public class Kata {
    public static boolean smallEnough(int[] a, int limit) {
        for (int num : a) {
            if (num > limit) {
                return false;
            }
        }
        return true;
    }
}