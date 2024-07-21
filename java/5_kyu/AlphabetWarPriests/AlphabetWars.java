// https://www.codewars.com/kata/59473c0a952ac9b463000064/train/java

import java.util.HashMap;

public class AlphabetWars {
    public static String woLoLoooooo(String battlefield) {
        HashMap<Character, Integer> soldiers = new HashMap<>();
        int balanceOfPower = 0;
        soldiers.put('w', 4);
        soldiers.put('p', 3);
        soldiers.put('b', 2);
        soldiers.put('s', 1);
        soldiers.put('m', -4);
        soldiers.put('q', -3);
        soldiers.put('d', -2);
        soldiers.put('z', -1);
        for (int i = 0, n = battlefield.length(); i < n; i++) {
            char alphabet = battlefield.charAt(i);
            if (!soldiers.containsKey(alphabet)) {
                continue;
            }
            if (checkPriests(battlefield, i)) {
                balanceOfPower += soldiers.get(alphabet);
            } else if (checkPriests(battlefield, i, 'j') && soldiers.get(alphabet) > 0) {
                balanceOfPower -= soldiers.get(alphabet);
            } else if (checkPriests(battlefield, i, 't') && soldiers.get(alphabet) < 0) {
                balanceOfPower += Math.abs(soldiers.get(alphabet));
            } else {
                balanceOfPower += soldiers.get(alphabet);
            }
        }
        if (balanceOfPower == 0)
            return "Let's fight again!";
        return balanceOfPower > 0 ? "Left side wins!" : "Right side wins!";
    }

    private static boolean checkPriests(String battlefield, int i) {
        if (i != 0 && i != battlefield.length() - 1) {
            return battlefield.charAt(i - 1) == 't' && battlefield.charAt(i + 1) == 'j'
                    || battlefield.charAt(i - 1) == 'j' && battlefield.charAt(i + 1) == 't';
        }
        return false;
    }

    private static boolean checkPriests(String battlefield, int i, char priest) {
        final int n = battlefield.length();
        return i != 0 && battlefield.charAt(i - 1) == priest || i != n - 1 && battlefield.charAt(i + 1) == priest;
    }

    public static void main(String[] args) {
        // Not part of the solution, just testing
        System.out.println(AlphabetWars.woLoLoooooo("z")); // => "z" => "Right side wins!"
        System.out.println(AlphabetWars.woLoLoooooo("tz")); // => "ts" => "Left side wins!"
        System.out.println(AlphabetWars.woLoLoooooo("jz")); // => "jz" => "Right side wins!"
        System.out.println(AlphabetWars.woLoLoooooo("zt")); // => "st" => "Left side wins!"
        System.out.println(AlphabetWars.woLoLoooooo("azt")); // => "ast" => "Left side wins!"
        System.out.println(AlphabetWars.woLoLoooooo("tzj")); // => "tzj" => "Right side wins!"
    }
}