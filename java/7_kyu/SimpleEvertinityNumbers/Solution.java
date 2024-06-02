// https://www.codewars.com/kata/5b93f268563417c7ed0001bd/train/java

import java.util.HashMap;

class Solution {
    public static int solve(int a, int b) {
        int count = 0;
        for (int i = a; i <= b; i++) {
            if (isEviternity(i)) {
                count++;
            }
        }
        return count;
    }

    private static boolean isEviternity(int n) {
        HashMap<Character, Integer> counts = new HashMap<>();
        counts.put('8', 0);
        counts.put('5', 0);
        counts.put('3', 0);
        String strNum = String.valueOf(n);
        for (int i = 0; i < strNum.length(); i++) {
            switch (strNum.charAt(i)) {
                case '8':
                    counts.put('8', counts.get('8') + 1);
                    break;
                case '5':
                    counts.put('5', counts.get('5') + 1);
                    break;
                case '3':
                    counts.put('3', counts.get('3') + 1);
                    break;
                default:
                    return false;
            }
        }
        return (counts.get('8') >= counts.get('5') &&
                counts.get('5') >= counts.get('3'));
    }

    public static void main(String[] args) {
        // Not part of the solution, just testing
        int[] testCases = new int[] { 100, 1000, 10000, 100000 };
        for (int i = 0; i < testCases.length; i++) {
            System.out.printf(
                "Test Case %s: %s\n", i + 1, solve(1, testCases[i])
            );
        }
    }
}
