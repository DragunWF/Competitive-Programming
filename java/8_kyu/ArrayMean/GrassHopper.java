// https://www.codewars.com/kata/55d277882e139d0b6000005d/train/java

public class GrassHopper {
    public static int findAverage(int[] nums) {
        int sum = 0;
        for (int num : nums)
            sum += num;
        return sum / nums.length;
    }
}