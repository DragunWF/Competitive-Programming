// https://www.codewars.com/kata/57a73e697cb1f31dd70000d2/train/java

import java.util.Arrays;

public class Kata {
    private static String[] animals = {
            "Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"
    };
    private static String[] elements = {
            "Wood", "Fire", "Earth", "Metal", "Water"
    };

    public static String chineseZodiac(int year) {
        return String.format("%s %s", animals[year % animals.length], elements[year % elements.length]);
    }

    public static void main(String[] args) {
        // Not part of the solution, just testing
        System.out.println(chineseZodiac(1965)); // Wood Snake
        System.out.println(chineseZodiac(1938)); // Earth Tiger
    }
}