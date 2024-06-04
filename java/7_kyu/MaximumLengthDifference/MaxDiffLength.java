// https://www.codewars.com/kata/5663f5305102699bad000056/train/java

class MaxDiffLength {
    public static int mxdiflg(String[] a1, String[] a2) {
        if (a1.length == 0 || a2.length == 0) return -1;
        return Math.max(Math.abs(getMaxLength(a1) - getMinLength(a2)),
                Math.abs(getMinLength(a1) - getMaxLength(a2)));
    }

    private static int getMaxLength(String[] arr) {
        return getTargetLength(arr, false);
    }

    private static int getMinLength(String[] arr) {
        return getTargetLength(arr, true);
    }

    private static int getTargetLength(String[] arr, boolean isMin) {
        int output = arr[0].length();
        for (int i = 1; i < arr.length; i++) {
            if (!isMin && arr[i].length() > output ||
                    isMin && arr[i].length() < output) {
                output = arr[i].length();
            }
        }
        return output;
    }
}