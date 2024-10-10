import java.util.*;
import java.io.*;

public class _1669B {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int t = input.nextInt();
        for (int i = 0; i < t; i++) {
            int n = input.nextInt();
            int[] a = intArr(input, n);
            System.out.println(solve(n, a));
        }
    }
    
    private static int[] intArr(Scanner input, int n) {
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) 
            arr[i] = input.nextInt();
        return arr;
    }
    
    private static int solve(int n, int[] a) {
        if (n < 3) return -1;
        HashMap<Integer, Integer> nums = new HashMap<>();
        for (int i = 0; i < n; i++) { 
            if (nums.containsKey(a[i])) { 
                nums.put(a[i], nums.get(a[i]) + 1);
                if (nums.get(a[i]) >= 3) return a[i];
            }
            else nums.put(a[i], 1);
        }
        return -1;
    }
}