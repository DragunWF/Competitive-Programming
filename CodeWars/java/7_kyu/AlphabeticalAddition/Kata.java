// https://www.codewars.com/kata/5d50e3914861a500121e1958/train/java

public class Kata {
    private static String[] alphabets = {
            "a", "b", "c", "d", "e", "f", "g", "h", "i",
            "j", "k", "l", "m", "n", "o", "p", "q", "r",
            "s", "t", "u", "v", "w", "x", "y", "z"
    };

    public static String addLetters(String... letters) {
        int total = 0;
        for (int i = 0; i < letters.length; i++) {
            total += getPos(letters[i]);
        }
        if (total == 0)
            return "z";
        return alphabets[--total >= alphabets.length ? total % alphabets.length : total];
    }

    private static int getPos(String str) {
        for (int i = 0, pos = 1; i < alphabets.length; i++, pos++) {
            if (str.equals(alphabets[i])) {
                return pos;
            }
        }
        return 0;
    }

    public static void main(String[] args) {
        // Not part of the solution, just testing
        System.out.println(addLetters("a", "b", "c")); // a
        System.out.println(addLetters("a", "z")); // f
        System.out.println(addLetters("u", "y", "r", "r", "b", "z", "f", "t", "s", "y")); // x
        System.out.println(addLetters("z", "r", "z", "m", "y", "u", "e", "z", "b", "u")); // a
    }
}