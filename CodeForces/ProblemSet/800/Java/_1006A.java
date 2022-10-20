import java.util.*;

public class _1006A {
    private static final Scanner input = new Scanner(System.in);

    public static void main(String[] args) {
        final int n = input.nextInt();
        final int[] arr = new int[n];
        for (int i = 0; i < n; i++)
            arr[i] = input.nextInt();
        solve(arr, n);
        displayArray(arr);
    }

    private static void solve(int[] arr, int n) {
        for (int i = 0; i < n; i++)
            if (arr[i] % 2 == 0)
                arr[i] -= 1;
    }

    private static void displayArray(int[] arr) {
        for (int num : arr)
            System.out.print(num + " ");
        System.out.println();
    }
}
