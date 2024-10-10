// https://www.codewars.com/kata/5672a98bdbdd995fad00000f/train/java

import java.util.HashMap;

public class Kata {
    public static String rps(String p1, String p2) {
        if (p1.equals(p2))
            return "Draw!";
        HashMap<String, String> choices = new HashMap<>();
        choices.put("rock", "paper");
        choices.put("paper", "scissors");
        choices.put("scissors", "rock");
        if (choices.get(p1).equals(p2))
            return "Player 2 won!";
        return "Player 1 won!";
    }

    public static void main(String[] args) {
        // Not part of the solution, just testing
        System.out.println(rps("rock", "paper"));
        System.out.println(rps("scissors", "paper"));
        System.out.println(rps("paper", "paper"));
    }
}
