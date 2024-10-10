// https://www.codewars.com/kata/582e0e592029ea10530009ce/train/java

public class Kata {
    public static String duckDuckGoose(Player[] players, int goose) {
        return players[(goose - 1) % players.length].name;
    }
}

class Player {
    public String name;
}