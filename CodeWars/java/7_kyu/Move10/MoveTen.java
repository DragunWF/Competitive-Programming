// https://www.codewars.com/kata/57cf50a7eca2603de0000090/train/java

import java.util.HashMap;

public class MoveTen {
  public static String moveTen(String s) {
    StringBuilder output = new StringBuilder();
    char[] alphabets = "abcdefghijklmnopqrstuvwxyz".toCharArray();
    HashMap<Character, Integer> alphabetMap = mapAlphabets(alphabets);
    for (int i = 0; i < s.length(); i++) {
        int alphabetIndex = alphabetMap.get(s.charAt(i));
        output.append(alphabets[(alphabetIndex + 10) % alphabets.length]);
    }
    return output.toString();
  }

  private static HashMap<Character, Integer> mapAlphabets(char[] alphabets) {
    HashMap<Character, Integer> map = new HashMap<>();
    for (int i = 0; i < alphabets.length; i++) {
        map.put(alphabets[i], i);
    }
    return map;
  }
}