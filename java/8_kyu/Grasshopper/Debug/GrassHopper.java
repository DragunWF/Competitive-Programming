// https://www.codewars.com/kata/55cb854deb36f11f130000e1/train/java

public class GrassHopper {
    public static String weatherInfo(int temp) {
        double c = convertToCelsius(temp);
        return c + (c > 0 ? " is above freezing temperature" : " is freezing temperature");
    }

    public static double convertToCelsius(int temperature) {
        return (temperature - 32) * (5 / 9.0);
    }

    public static void main(String[] args) {
        // Not part of the solution, just testing
        System.out.println(weatherInfo(50)); // "10.0 is above freezing temperature"
        System.out.println(weatherInfo(23)); // "-5.0 is freezing temperature"
    }
}