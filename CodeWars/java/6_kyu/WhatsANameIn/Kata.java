// https://www.codewars.com/kata/59daf400beec9780a9000045/train/java

public class Kata {
    public static boolean nameInStr(String str, String name) {
        int currentPlace = 0;
        str = str.toLowerCase();
        name = name.toLowerCase();
        for (int i = 0; i < str.length(); i++) {
            if (str.charAt(i) == name.charAt(currentPlace))
                currentPlace++;
            if (currentPlace >= str.length())
                break;
        }
        return currentPlace == name.length();
    }

    public static void main(String[] args) {
        // Not part of the solution, just testing
        System.out.println(nameInStr("Across the rivers", "chris"));
    }
}