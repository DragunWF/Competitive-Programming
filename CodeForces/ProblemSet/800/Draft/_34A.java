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

    private static int getIndex(int[] arr, int firstIndex, boolean getMax) {
        int targetIndex = -1;
        int targetNum = getMax ? -1 : 1001;
        for (int i = 0; i < arr.length; i++) {
            if (!getMax && arr[i] <= targetNum && i != firstIndex
                    || getMax && arr[i] >= targetNum && i != firstIndex) {
                targetNum = arr[i];
                targetIndex = i;
            }
        }
        return targetIndex;
    }

    private static String solve(int[] arr) {
        final int minIndex = getIndex(arr, -1, false);
        final int secondMinIndex = getIndex(arr, minIndex, false);
        final int minDiff = Math.abs(arr[minIndex] - arr[secondMinIndex]);

        final int maxIndex = getIndex(arr, -1, true);
        final int secondMaxIndex = getIndex(arr, maxIndex, true);
        final int maxDiff = Math.abs(arr[maxIndex] - arr[secondMaxIndex]);

        final int diff = Math.min(minDiff, maxDiff);
        final int index = diff == minDiff ? minIndex : maxIndex;
        final int secondIndex = diff == minDiff ? secondMinIndex : secondMaxIndex;

        return String.format("%s %s", index + 1, secondIndex + 1);
    }
}
