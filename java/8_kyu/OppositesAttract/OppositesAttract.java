// https://www.codewars.com/kata/555086d53eac039a2a000083/train/java

public class OppositesAttract {
    public static boolean isLove(final int flower1, final int flower2) {
        return flower1 % 2 == 0 && flower2 % 2 != 0 || flower1 % 2 != 0 && flower2 % 2 == 0;
    }
}
