// https://www.codewars.com/kata/5938f5b606c3033f4700015a/train/java

import java.util.HashMap;

public class AlphabetWarAirstrike {
    public static String alphabetWar(String fight) {
        StringBuilder afterBomb = new StringBuilder();
        for (int i = 0, n = fight.length(); i < n; i++) {
            if (i != 0 && fight.charAt(i - 1) == '*' || i != n - 1 && fight.charAt(i + 1) == '*') {
                afterBomb.append('_');
            } else {
                afterBomb.append(fight.charAt(i));
            }
        }
        return battle(afterBomb.toString());
    }

    private static String battle(String battleField) {
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
        for (char alphabet : battleField.toCharArray()) {
            if (soldiers.containsKey(alphabet)) {
                balanceOfPower += soldiers.get(alphabet);
            }
        }
        if (balanceOfPower == 0)
            return "Let's fight again!";
        return balanceOfPower > 0 ? "Left side wins!" : "Right side wins!";
    }

    public static void main(String[] args) {
        // Not part of the solution, just testing
        System.out.println(alphabetWar("s*zz")); // => Right side wins!
        System.out.println(alphabetWar("*zd*qm*wp*bs*")); // => Let's fight again!
        System.out.println(alphabetWar("zzzz*s*")); // => Right side wins!
        System.out.println(alphabetWar("www*www****z")); // => Left side wins!
    }
}