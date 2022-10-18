import java.util.*;

public class _1608A {
    private static final Scanner input = new Scanner(System.in);

    public static void main(String[] args) {
        final int t = input.nextInt();
        for (int i = 0; i < t; i++) {
            final int n = input.nextInt();
            System.out.println(solve(n));
        }
    }

    private static String solve(int n) {
        String output = "";
        for (int i = 2; i < n + 2; i++)
            output += i + " ";
        return output;
    }
}
