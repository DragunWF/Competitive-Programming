// https://www.codewars.com/kata/569b5cec755dd3534d00000f/train/java

public class NewAverage {
    public static long newAvg(double[] arr, double navg) throws Exception {
        double sum = 0;
        for (int i = 0; i < arr.length; i++) {
            sum += arr[i];
        }

        double requiredDonation = navg * (arr.length + 1) - sum;
        if (requiredDonation <= 0) {
            throw new IllegalArgumentException();
        }
        return (long) Math.ceil(requiredDonation);
    }

    public static void main(String[] args) throws Exception {
        // Not part of the solution, just testing
        double[] a = new double[] { 14, 30, 5, 7, 9, 11, 15 };
        System.out.println(newAvg(a, 90));
        System.out.println(newAvg(a, 92));
    }
}