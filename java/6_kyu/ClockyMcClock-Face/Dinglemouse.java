// https://www.codewars.com/kata/59752e1f064d1261cb0000ec/train/java

public class Dinglemouse {
    public static String whatTimeIsIt(final double angle) {
        int hour = (int) Math.floor((angle / 30));
        int minute = (int) (((angle % 30) / 30) * 60);
        String minuteStr = minute < 10 ? "0" + minute : String.valueOf(minute);
        String hourStr;
        if (hour == 0) {
            hourStr = "12";
        } else {
            hourStr = hour < 10 ? "0" + hour : String.valueOf(hour);
        }
        return String.format("%s:%s", hourStr, minuteStr);
    }

    public static void main(final String[] args) {
        // Not part of the solution, just testing
        double[] testCases = { 0, 90, 180, 270, 360, 184 };
        for (int i = 0, j = 1; i < testCases.length; i++, j++) {
            System.out.printf("Test Case #%s: %s = %s degrees\n",
                    j, whatTimeIsIt(testCases[i]), testCases[i]);
        }
    }
}