// https://www.codewars.com/kata/558fa34727c2d274c10000ae/train/java

import java.util.HashMap;

public class Kata {
    public static int scrabbleScore(String word) {
        HashMap<Character, Integer> letterScores = getLetterScores();
        int score = 0;
        word = word.toUpperCase();
        for (int i = 0; i < word.length(); i++) {
            char letter = word.charAt(i);
            if (letter >= 'A' && letter <= 'Z') {
                score += letterScores.get(letter);
            }
        }
        return score;
    }

    private static HashMap<Character, Integer> getLetterScores() {
        HashMap<Character, Integer> output = new HashMap<>();
        mapLetterPoints(output, "AEIOULNRST".toCharArray(), 1);
        mapLetterPoints(output, "DG".toCharArray(), 2);
        mapLetterPoints(output, "BCMP".toCharArray(), 3);
        mapLetterPoints(output, "FHVWY".toCharArray(), 4);
        mapLetterPoints(output, "K".toCharArray(), 5);
        mapLetterPoints(output, "JX".toCharArray(), 8);
        mapLetterPoints(output, "QZ".toCharArray(), 10);
        return output;
    }

    private static void mapLetterPoints(HashMap<Character, Integer> letterScores, char[] letters, int score) {
        for (char letter : letters) {
            letterScores.put(letter, score);
        }
    }

    public static void main(String[] args) {
        // Not part of the solution, just testing
        System.out.println(scrabbleScore("cabb age")); // 14
    }
}