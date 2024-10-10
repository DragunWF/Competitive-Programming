// https://www.codewars.com/kata/5270d0d18625160ada0000e4/train/java

import java.util.HashMap;

public class Greed {
    public static int greedy(int[] dice) {
        int[] diceValues = new int[6];
        for (int i = 0; i < dice.length; i++) {
            diceValues[dice[i] - 1]++;
        }
        return calculatePoints(diceValues);
    }

    private static int calculatePoints(int[] values) {
        int points = 0;
        HashMap<Integer, Integer> threeRewards = new HashMap<>();
        HashMap<Integer, Integer> oneRewards = new HashMap<>();
        threeRewards.put(1, 1000);
        threeRewards.put(2, 200);
        threeRewards.put(3, 300);
        threeRewards.put(4, 400);
        threeRewards.put(5, 500);
        threeRewards.put(6, 600);
        oneRewards.put(1, 100);
        oneRewards.put(5, 50);
        for (int i = 0, diceValue = 1; i < values.length; i++, diceValue++) {
            if (oneRewards.containsKey(diceValue)) {
                points += (values[i] % 3) * oneRewards.get(diceValue);
            }
            points += (values[i] / 3) * threeRewards.get(diceValue);
        }
        return points;
    }

    public static void main(String[] args) {
        // Not part of the solution, just testing
        System.out.println(greedy(new int[] { 5, 1, 3, 4, 1 }));
    }
}