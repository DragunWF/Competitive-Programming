import java.util.*;

public class _34A {
    private static final Scanner input = new Scanner(System.in);

    public static void main(String[] args) {
        final int n = input.nextInt();
        final int[] arr = new int[n];
        for (int i = 0; i < n; i++)
            arr[i] = input.nextInt();
        System.out.println(solve(arr));
    }

    private static String solve(int[] arr) {
        int firstIndex = -1;
        int secondIndex = -2;
        int minDiff = 1001;

        for (int i = 1; i < arr.length; i++) {
            final int diff = Math.abs(arr[i] - arr[i - 1]);
            if (diff < minDiff) {
                minDiff = diff;
                firstIndex = i;
                secondIndex = i - 1;
            }
        }

        if (Math.abs(arr[0] - arr[arr.length - 1]) < minDiff) {
            firstIndex = 0;
            secondIndex = arr.length - 1;
        }

        return String.format("%s %s", firstIndex + 1, secondIndex + 1);
    }
}
