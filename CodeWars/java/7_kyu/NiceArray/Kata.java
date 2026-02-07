// https://www.codewars.com/kata/59b844528bcb7735560000a0/train/java

public class Kata{
    public static boolean isNice(Integer[] arr) {
        if (arr.length == 0) return false;
        for (int i = 0; i < arr.length; i++) {
            if (!isAdjacentNumExist(arr, arr[i])) {
                return false;
            }
        }
        return true;
    }

    public static boolean isAdjacentNumExist(Integer[] arr, int target) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == target - 1 || arr[i] == target + 1) {
                return true;
            }
        }
        return false;
    }
}