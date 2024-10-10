// https://www.codewars.com/kata/58539230879867a8cd00011c/train/java

import java.util.HashMap;

class WhereIsMyParent {
    private static String findChildren(final String text) {
        HashMap<Character, Integer> childCount = new HashMap<>(); // Key: Parent, Children: Count
        for (char letter : text.toCharArray()) {
            if (isParent(letter)) {
                childCount.put(letter, 0);
            }
        }
        for (char letter : text.toCharArray()) {
            if (!isParent(letter)) {
                char upperCase = (char) (letter - 32);
                childCount.put(upperCase, childCount.get(upperCase) + 1);
            }
        }
        return getSortedPeople(childCount);
    }

    private static String getSortedPeople(HashMap<Character, Integer> people) {
        StringBuilder output = new StringBuilder();
        for (int i = 65; i <= 90; i++) { // ASCII char code, range of uppercase letters
            char parent = (char) i;
            if (people.containsKey(parent)) {
                output.append(parent);
                for (int j = 0; j < people.get(parent); j++) {
                    output.append((char) (i + 32)); // Convert to lowercase
                }
            }
        }
        return output.toString();
    }

    private static boolean isParent(char letter) {
        return letter >= 65 && letter <= 90;
    }

    public static void main(String[] args) {
        // Not part of the solution, just testing
        System.out.println(findChildren("aAbaBb"));
    }
}
