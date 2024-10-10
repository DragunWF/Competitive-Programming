// https://www.codewars.com/kata/57cfdf34902f6ba3d300001e/train/java

import java.util.Arrays;

public class SortAndStar {
    public static String twoSort(String[] s) {
        Arrays.sort(s);
        return String.join("***", s[0].split(""));
    }

    public static void main(String[] args) {
        // test code, not part of the actual solution
        System.out.println(twoSort(
                new String[] { "bitcoin", "take", "over", "the", "world", "maybe", "who", "knows", "perhaps" }));
    }
}
