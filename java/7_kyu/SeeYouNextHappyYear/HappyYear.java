// https://www.codewars.com/kata/5ae7e3f068e6445bc8000046/train/java 

import java.util.HashSet;

public class HappyYear {
    static public int nextHappyYear(int year) {
        year++;
        while (!isHappyYear(year))
            year++;
        return year;
    }

    static private boolean isHappyYear(int year) {
        String strNum = String.valueOf(year);
        HashSet<Character> unique = new HashSet<>();
        for (int i = 0; i < strNum.length(); i++) {
            unique.add(strNum.charAt(i));
        }
        return unique.size() == strNum.length();
    }

    public static void main(String[] args) {
        // Not part of the solution, just testing
        System.out.println(nextHappyYear(1001)); // 1023
    }
}
