// https://www.codewars.com/kata/564e7fc20f0b53eb02000106/train/java

public class Consonants {
    public static int getCount(String str) {
        char[] consonants = "bcdfghjklmnpqrstvwxyz".toCharArray();
        int count = 0;
        for (char item : str.toLowerCase().toCharArray()) {
            if (contains(consonants, item)) {
                count++;
            }
        }
        return count;
    }

    private static boolean contains(char[] arr, char target) {
        for (char item : arr) {
            if (item == target) {
                return true;
            }
        }
        return false;
    }
}