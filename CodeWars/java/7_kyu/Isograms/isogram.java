// https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/java

import java.util.ArrayList;

public class isogram {
    public static boolean isIsogram(String str) {
        if (str.length() == 0)
            return true;
        str = str.toLowerCase();
        ArrayList<Character> characters = new ArrayList<>();
        for (int i = 0, n = str.length(); i < n; i++) {
            if (characters.contains(str.charAt(i)))
                return false;
            characters.add(str.charAt(i));
        }
        return true;
    }
}
