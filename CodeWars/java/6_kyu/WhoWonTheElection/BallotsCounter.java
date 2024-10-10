// https://www.codewars.com/kata/554910d77a3582bbe300009c/train/java

import java.util.List;
import java.util.HashMap;

public class BallotsCounter {
    public static String getWinner(final List<String> listOfBallots) {
        HashMap<String, Integer> votes = new HashMap<>();
        for (String name : listOfBallots) {
            if (votes.containsKey(name)) {
                votes.put(name, votes.get(name) + 1);
            } else {
                votes.put(name, 1);
            }
        }
        return getWinner(votes, listOfBallots.size());
    }

    private static String getWinner(HashMap<String, Integer> votes, int n) {
        int mostVotes = 0;
        String winner = null;
        for (String name : votes.keySet()) {
            if (votes.get(name) > n / 2 && votes.get(name) > mostVotes) {
                mostVotes = votes.get(name);
                winner = name;
            }
        }
        return winner;
    }
}