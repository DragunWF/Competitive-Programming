// https://www.codewars.com/kata/5601409514fc93442500010b/train/java

public class Kata {
    public static boolean betterThanAverage(int[] classPoints, int yourPoints) {
        int sum = 0;
        for (int score : classPoints)
            sum += score;
        return yourPoints > sum / classPoints.length;
    }
}