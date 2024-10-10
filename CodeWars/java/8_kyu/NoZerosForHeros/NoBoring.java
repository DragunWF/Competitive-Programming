// https://www.codewars.com/kata/570a6a46455d08ff8d001002/train/java

public class NoBoring {
    public static int noBoringZeros(int n) {
        if (n == 0)
            return 0;
        String strNum = String.valueOf(n);
        int stopIndex = 0;
        for (int i = strNum.length() - 1; i >= 0; i--) {
            if (strNum.charAt(i) != '0') {
                stopIndex = i;
                break;
            }
        }
        return Integer.parseInt(strNum.substring(0, stopIndex + 1));
    }
}