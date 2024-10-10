// https://www.codewars.com/kata/5853213063adbd1b9b0000be/train/java

import java.util.Arrays;

public class Solution {
    public static String[] streetFighterSelection(String[][] fighters, int[] position, String[] moves) {
        String[] chosen = new String[moves.length];
        final int MAX_HEIGHT = fighters.length, MAX_WIDTH = fighters[0].length;

        // Fills in the characters that went through selection within the "chosen" array
        for (int i = 0; i < moves.length; i++) {
            String move = moves[i];

            // Checks the move set and updates the current position
            if (move == "left" || move == "right") {
                position[0] += move == "right" ? 1 : -1;

                // Circulates the position if it goes out of bounds
                if (position[0] >= MAX_WIDTH)
                    position[0] = 0;
                else if (position[0] < 0)
                    position[0] = MAX_WIDTH - 1;
            } else {
                int prevValue = position[1];
                position[1] += move == "up" ? -1 : 1;

                // Undos the move if vertical movement goes out of bounds
                if (position[1] >= MAX_HEIGHT || position[1] < 0)
                    position[1] = prevValue;
            }
            chosen[i] = fighters[position[1]][position[0]];
        }

        return chosen;
    }

    public static void main(String[] args) {
        // Not part of the solution, just testing
        String[][] fighters = new String[][] {
                new String[] { "Ryu", "E.Honda", "Blanka", "Guile", "Balrog", "Vega" },
                new String[] { "Ken", "Chun Li", "Zangief", "Dhalsim", "Sagat", "M.Bison" },
        };
        // Expected Output: { "Ryu", "Vega", "Ryu", "Vega", "Balrog" }
        System.out.println(Arrays.toString(streetFighterSelection(
                fighters, new int[] { 0, 0 }, new String[] { "up", "left", "right", "left", "left" })));
    }
}