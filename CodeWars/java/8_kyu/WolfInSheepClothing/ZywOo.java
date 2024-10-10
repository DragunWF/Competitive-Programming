// https://www.codewars.com/kata/5c8bfa44b9d1192e1ebd3d15/train/java

public class ZywOo {
    public static String warnTheSheep(String[] array) {
        for (int i = array.length - 1, n = 1; i > 0; i--, n++) {
            if (array[i - 1].equals("wolf")) {
                return String.format("Oi! Sheep number %s! You are about to be eaten by a wolf!", n);
            }
        }
        return "Pls go away and stop eating my sheep";
    }
}