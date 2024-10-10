// https://www.codewars.com/kata/64fc03a318692c1333ebc04c/train/java

public class Kata {
    public static boolean bestFriend(String txt, char a, char b) {
        for (int i = 0, n = txt.length(); i < n; i++) {
            if (txt.charAt(i) == a && !(i != n - 1 && txt.charAt(i + 1) == b)) {
                return false;
            }
        }
        return true;
    }
}