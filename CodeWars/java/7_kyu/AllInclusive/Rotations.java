// https://www.codewars.com/kata/5700c9acc1555755be00027e/train/java

import java.util.List;
import java.util.ArrayList;

public class Rotations {
    public static boolean containAllRots(String str, List<String> arr) {
        if (str.isEmpty()) {
            return true;
        }

        List<String> allRotations = getRotations(str);
        for (String rotation : allRotations) {
            if (!arr.contains(rotation)) {
                return false;
            }
        }
        return true;
    }

    private static List<String> getRotations(String str) {
        List<String> rotations = new ArrayList<>();
        rotations.add(str);
        String currentRotation = str;
        for (int i = 1; i < str.length(); i++) {
            currentRotation = rotate(currentRotation);
            rotations.add(currentRotation);
        }
        return rotations;
    }

    private static String rotate(String str) {
        StringBuilder rotatedStr = new StringBuilder();
        rotatedStr.append(str.charAt(str.length() - 1));
        for (int i = 1; i < str.length(); i++) {
            rotatedStr.append(str.charAt(i - 1));
        }
        return rotatedStr.toString();
    }

    public static void main(String[] args) {
        System.out.println(getRotations("abcd").toString());
        System.out.println(rotate("abcd"));
    }
}