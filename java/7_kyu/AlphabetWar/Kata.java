// https://www.codewars.com/kata/59377c53e66267c8f6000027/train/java

import java.util.HashMap;

public class Kata {
    public static String alphabetWar(String fight) {
        HashMap<Character, Integer> leftPower = new HashMap<>();
        HashMap<Character, Integer> rightPower = new HashMap<>();

        leftPower.put('w', 4);
        leftPower.put('p', 3);
        leftPower.put('b', 2);
        leftPower.put('s', 1);

        rightPower.put('m', 4);
        rightPower.put('q', 3);
        rightPower.put('d', 2);
        rightPower.put('z', 1);

        int balance = 0;
        for (int i = 0, n = fight.length(); i < n; i++) {
            if (leftPower.containsKey(fight.charAt(i))) {
                balance += leftPower.get(fight.charAt(i));
            } else if (rightPower.containsKey(fight.charAt(i))) {
                balance -= rightPower.get(fight.charAt(i));
            }
        }

        if (balance == 0)
            return "Let's fight again!";
        return balance > 0 ? "Left side wins!" : "Right side wins!";
    }
}