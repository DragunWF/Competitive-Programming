// https://www.codewars.com/kata/59dd3ccdded72fc78b000b25/train/java

public class DayOfWeek {
    public static String getDay(int n) {
        if (n <= 0 || n > 7) {
            return "Wrong, please enter a number between 1 and 7";
        }
        return new String[] { "Sunday", "Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday" }[n - 1];
    }
}