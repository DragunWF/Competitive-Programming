// https://www.codewars.com/kata/595519279be6c575b5000016/train/java

public class BattleOfTheCharacters {
    public static String battle(final String x, final String y) {
        int xPower = getPowerLevel(x);
        int yPower = getPowerLevel(y);
        if (xPower == yPower) {
            return "Tie!";
        }
        return xPower > yPower ? x : y;
    }

    private static int getPowerLevel(String str) {
        int power = 0;
        for (int i = 0; i < str.length(); i++) {
            power += ((int) (str.charAt(i))) - 64;
        }
        return power;
    }

    public static void main(String[] args) {
        System.out.println(battle("PL", "V"));
    }
}