// https://www.codewars.com/kata/59f061773e532d0c87000d16/train/java

public class Kata {
    public static int elevatorDistance(int[] arr) {
        int distance = 0;
        for (int i = 1; i < arr.length; i++) {
            distance += Math.abs(arr[i] - arr[i - 1]);
        }
        return distance;
    }
}