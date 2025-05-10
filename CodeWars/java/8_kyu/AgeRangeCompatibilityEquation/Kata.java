// https://www.codewars.com/kata/5803956ddb07c5c74200144e/train/java

public class Kata {
    public static String datingRange(int age) {
        int min, max;
        if (age <= 14) {
            min = (int) Math.floor(age - 0.1 * age);
            max = (int) Math.floor(age + 0.1 * age);
        } else {
            min = (int) Math.floor(age / 2.0 + 7);
            max = 2 * (age - 7);
        }
        return String.format("%s-%s", min, max);
    }
}