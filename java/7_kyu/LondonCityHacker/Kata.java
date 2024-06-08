// https://www.codewars.com/kata/5bce125d3bb2adff0d000245/train/java

public class Kata {
    public static String londonCityHacker(Object[] journey) {
        double cost = 0;
        boolean recentBus = false;
        for (Object ticket : journey) {
            if (ticket instanceof String) {
                recentBus = false;
                cost += 2.4;
            } else if (!recentBus) {
                recentBus = true;
                cost += 1.5;
            } else {
                recentBus = false;
            }
        }
        return String.format("£%.2f", cost);
    }

    public static void main(String[] args) {
        // Not part of the solution, just testing
        System.out.println(londonCityHacker(new Object[] { "Northern", "Central", 243, 1, "Victoria" }));
        System.out.println(londonCityHacker(new Object[] { "Piccadilly", 56, 93, 243, 20, 14 }));
    }
}