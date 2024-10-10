import java.util.*;
import java.lang.*;
import java.io.*;

public class CodeForces {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int t = input.nextInt();
        for (int i = 0; i < t; i++) {
            int n = input.nextInt();
            input.nextLine();
            int[] a = intArr(input.nextLine().split(" "), n);
            System.out.println(solve(n, a));
        }
    }
    
    private static int[] intArr(String[] line, int n) {
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) 
            arr[i] = Integer.parseInt(line[i]);
        return arr;
    }
    
    private static int solve(int n, int[] a) {
        if (n < 3) return -1;
        Arrays.sort(a);
        int output = 0;
        int repeats = 1;
        for (int i = 1; i < n; i++) {
            if (a[i - 1] == a[i]) repeats++;
            else repeats = 1;
            if (repeats >= 3) { 
                output++;
                repeats = 1;
            }
        }
        return output != 0 ? output : -1;
    }
}