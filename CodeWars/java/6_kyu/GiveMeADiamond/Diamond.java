// https://www.codewars.com/kata/5503013e34137eeeaa001648/train/java

class Diamond {
    public static String print(int n) {
        if (n < 0 || n % 2 == 0)
            return null;
        String output = "";
        int min = n / 2 + 1;
        int max = min;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= max; j++) {
                output += j >= min ? "*" : " ";
            }
            output += "\n";
            if (i < (n / 2 + 1)) {
                min--;
                max++;
            } else {
                min++;
                max--;
            }
        }
        return output;
    }

    public static String previousPrint(int n) {
        if (n < 0 || n % 2 == 0)
            return null;
        String output = "";
        int min = n / 2 + 1;
        int max = min;
        for (int i = 1; i <= n; i++) {
            System.out.println(max);
            for (int j = 1; j <= max; j++) {
                System.out.println(j);
                output += j >= min ? "*" : " ";
            }
            if (i != n)
                output += "\n";
            if (i < (n / 2 + 1)) {
                min--;
                max++;
            } else {
                min++;
                max--;
            }
        }
        return output;
    }

    // Test method
    public static void main(String[] args) {
        int[] testCases = { 5 }; // { -2, 3, 5, 9 }
        for (int n : testCases) {
            System.out.println(print(n));
        }
    }
}