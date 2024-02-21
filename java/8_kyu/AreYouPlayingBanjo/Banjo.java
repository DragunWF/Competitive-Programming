// https://www.codewars.com/kata/53af2b8861023f1d88000832/train/java

public class Banjo {
    public static String areYouPlayingBanjo(String name) {
        String phrase = name.toLowerCase().charAt(0) == 'r' ? "plays banjo" : "does not play banjo";
        return String.format("%s %s", name, phrase);
    }
}
