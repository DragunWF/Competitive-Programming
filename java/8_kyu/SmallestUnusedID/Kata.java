// https://www.codewars.com/kata/55eea63119278d571d00006a/train/java

import java.util.Arrays;

public class Kata {
    public static int nextId(int[] ids) {
        Arrays.sort(ids);
        if (ids.length == 0 || ids[0] != 0)
            return 0;
        for (int i = 1, last = ids[0]; i < ids.length; last = ids[i++]) {
            if (last + 1 < ids[i]) {
                return last + 1;
            }
        }
        return ids[ids.length - 1] + 1;
    }

    public static void main(String[] args) {
        // Not part of the solution, just testing
        System.out.println(nextId(new int[] { 1, 2, 0, 2, 3 }));
    }
}

// Previous Solution

// import java.util.Arrays;

// public class Kata {
// public static int nextId(int[] ids) {
// Arrays.sort(ids);
// if (ids.length == 0 || ids[0] != 0)
// return 0;
// int last = ids[0];
// for (int i = 1; i < ids.length; i++) {
// if (last + 1 < ids[i]) {
// return last + 1;
// } else if (ids[i] != 0) {
// last = ids[i];
// }
// }
// return last + 1;
// }
// }