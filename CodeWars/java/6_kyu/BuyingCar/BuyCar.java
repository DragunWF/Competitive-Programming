// https://www.codewars.com/kata/554a44516729e4d80b000012/train/java

public class BuyCar {
    public static int[] nbMonths(double startPriceOld, double startPriceNew, int savingPerMonth,
            double percentLossByMonth) {
        int savings = 0;
        int months = 0;
        while ((savings + startPriceOld) < startPriceNew) {
            savings += savingPerMonth;
            startPriceOld -= startPriceOld * (percentLossByMonth / 100);
            startPriceNew -= startPriceNew * (percentLossByMonth / 100);
            if (months % 2 == 0) {
                percentLossByMonth += 0.5;
            }
            months++;
        }
        return new int[] { months, (int) Math.round(savings + startPriceOld - startPriceNew) };
    }

    public static void main(String[] args) {
        // test code, not part of the solution
        int[] output = nbMonths(2000, 8000, 1000, 1.5);
        int[] second = nbMonths(12000, 8000, 1000, 1.5);
        System.out.printf("%s %s\n", output[0], output[1]);
        System.out.printf("%s %s\n", second[0], second[1]);
    }
}
