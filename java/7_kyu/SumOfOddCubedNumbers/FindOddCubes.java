// https://www.codewars.com/kata/580dda86c40fa6c45f00028a/train/java

public class FindOddCubes {
    public static int cubeOdd(int arr[]) {
        int sum = 0;
        for (int num : arr) {
            if (num % 2 != 0) {
                sum += num * num * num;
            }
        }
        return sum;
    }
}