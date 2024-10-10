// https://codewars.com/kata/57a429e253ba3381850000fb/train/java

public class Calculate {
    public static String bmi(double weight, double height) {
        double bmi = weight / Math.pow(height, 2);
        if (bmi <= 18.5)
            return "Underweight";
        if (bmi <= 25.0)
            return "Normal";
        if (bmi <= 30.0)
            return "Overweight";
        return "Obese";
    }
}