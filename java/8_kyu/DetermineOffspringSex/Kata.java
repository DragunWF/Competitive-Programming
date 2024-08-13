// https://www.codewars.com/kata/56530b444e831334c0000020/train/java

public class Kata {
    public static String chromosomeCheck(String sperm) {
        return sperm.equals("XX") ? "Congratulations! You're going to have a daughter."
                : "Congratulations! You're going to have a son.";
    }
}