// https://www.codewars.com/kata/54a2e93b22d236498400134b/train/java

/*
------- ------- -------
|     | | ABC | | DEF |
|  1  | |  2  | |  3  |
------- ------- -------
------- ------- -------
| GHI | | JKL | | MNO |
|  4  | |  5  | |  6  |
------- ------- -------
------- ------- -------
|PQRS | | TUV | | WXYZ|
|  7  | |  8  | |  9  |
------- ------- -------
------- ------- -------
|  *  | |space| |  #  |
|     | |  0  | |     |
------- ------- ------- 
*/

import java.util.HashMap;

public class Keypad {
    public static int presses(String phrase) {
        // Number of presses and button
        int numberOfPresses = 0;
        HashMap<Integer, char[]> presses = new HashMap<>();
        presses.put(1, new char[] { 'a', 'd', 'g', 'j', 'm', 'p', 't', 'w', ' ', '*', '#' });
        presses.put(2, new char[] { 'b', 'e', 'h', 'k', 'n', 'q', 'u', 'x' });
        presses.put(3, new char[] { 'c', 'f', 'i', 'l', 'o', 'r', 'v', 'y' });
        presses.put(4, new char[] { 's', 'z' });
        phrase = phrase.toLowerCase();
        for (int i = 0, n = phrase.length(); i < n; i++) {
            if (isDigit(phrase.charAt(i))) {
                switch (phrase.charAt(i)) {
                    case '0':
                        numberOfPresses += 2;
                        break;
                    case '1':
                        numberOfPresses++;
                        break;
                    default:
                        numberOfPresses += 4;
                }
                continue;
            }
            for (int points = 1; points <= presses.size(); points++) {
                if (isContains(presses.get(points), phrase.charAt(i))) {
                    numberOfPresses += points;
                    break;
                }
            }
        }
        return numberOfPresses;
    }

    private static boolean isContains(char[] arr, char target) {
        for (char element : arr) {
            if (target == element) {
                return true;
            }
        }
        return false;
    }

    private static boolean isDigit(char character) {
        return character >= 48 && character <= 57;
    }

    public static void main(String[] args) {
        // Not part of the solution, just testing
        String[] testCases = new String[] {
                "LOL", // 9
                "WHERE DO U WANT 2 MEET L8R" // 47
        };
        for (int i = 0, nth = 1; i < testCases.length; i++, nth++) {
            System.out.printf("%s: %s\n", nth, presses(testCases[i]));
        }
    }
}
