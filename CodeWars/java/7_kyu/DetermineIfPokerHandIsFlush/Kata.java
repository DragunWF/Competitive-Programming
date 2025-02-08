// https://www.codewars.com/kata/5acbc3b3481ebb23a400007d/train/java

public class Kata {
    public static boolean CheckIfFlush(String[] cards) {
        for (int i = 1; i < cards.length; i++) {
            int firstLastIndex = cards[i].length() - 1;
            int secondLastIndex = cards[i - 1].length() - 1;
            if (cards[i].charAt(firstLastIndex) != cards[i - 1].charAt(secondLastIndex)) {
                return false;
            }
        }
        return true;
    }
}