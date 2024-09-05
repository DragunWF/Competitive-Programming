// https://www.codewars.com/kata/53f1015fa9fe02cbda00111a/train/java

public class Ghost {
    private static String[] colors = { "white", "yellow", "purple", "red" };

    public String getColor() {
        return colors[(int) (Math.random() * colors.length)];
    }
}