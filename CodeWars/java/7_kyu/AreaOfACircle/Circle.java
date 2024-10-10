// https://www.codewars.com/kata/537baa6f8f4b300b5900106c/train/java

public class Circle {
    public static double area(double radius) {
        if (radius <= 0)
            throw new IllegalArgumentException();
        return Math.PI * Math.pow(radius, 2.0);
    }
}