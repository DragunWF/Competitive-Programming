// https://www.codewars.com/kata/593e2077edf0d3e2d500002d/train/java

import java.util.Arrays; // For testing

public class AlphabetWars {
    public static String reinforcesMassacre(String[] reinforces, String[] airstrikes) {
        int[] timesBombed = new int[reinforces[0].length()];
        for (String targets : airstrikes) {
            boolean[] bombed = new boolean[timesBombed.length];
            for (int i = 0, n = targets.length(); i < n; i++) {
                if (targets.charAt(i) == '*') {
                    bombed[i] = true;
                    if (i != 0)
                        bombed[i - 1] = true;
                    if (i != bombed.length - 1)
                        bombed[i + 1] = true;
                }
            }
            for (int i = 0; i < bombed.length; i++) {
                if (bombed[i]) {
                    timesBombed[i]++;
                }
            }
        }
        StringBuilder output = new StringBuilder();
        for (int i = 0; i < timesBombed.length; i++) {
            int bombCount = timesBombed[i];
            output.append(bombCount >= reinforces.length ? '_' : reinforces[bombCount].charAt(i));
        }
        return output.toString();
    }

    public static void main(String[] args) {
        // Not part of the solution, just testing
        System.out.println(
                reinforcesMassacre(
                        new String[] { "abcdefg", "hijklmn" },
                        new String[] { "   *   ", "*  *   " }));
        System.out.println(reinforcesMassacre(
                new String[] { "g964xxxxxxxx",
                        "myjinxin2015",
                        "steffenvogel",
                        "smile67xxxxx",
                        "giacomosorbi",
                        "freywarxxxxx",
                        "bkaesxxxxxxx",
                        "vadimbxxxxxx",
                        "zozofouchtra",
                        "colbydauphxx" },
                new String[] { "* *** ** ***",
                        " ** * * * **",
                        " * *** * ***",
                        " **  * * ** ",
                        "* ** *   ***",
                        "***   ",
                        "**",
                        "*",
                        "*" }));
    }
}