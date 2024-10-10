// https://www.codewars.com/kata/57ed4cef7b45ef8774000014/train/java

import java.util.HashMap;

public class TheOffice {
    public static String boredom(Person[] staff) {
        HashMap<String, Integer> boredomScores = new HashMap<>();
        boredomScores.put("accounts", 1);
        boredomScores.put("finance", 2);
        boredomScores.put("canteen", 10);
        boredomScores.put("regulation", 3);
        boredomScores.put("trading", 6);
        boredomScores.put("change", 6);
        boredomScores.put("IS", 8);
        boredomScores.put("retail", 5);
        boredomScores.put("cleaning", 4);
        boredomScores.put("pissing about", 25);
        int totalBoredom = 0;
        for (Person person : staff) {
            totalBoredom += boredomScores.get(person.department);
        }
        if (totalBoredom <= 80) {
            return "kill me now";
        }
        if (totalBoredom < 100 && totalBoredom > 80) {
            return "i can handle this";
        }
        return "party time!!";
    }
}

class Person {
    public String name; // name of the staff member
    public String department; // department they work in

    public Person(String name, String department) {
        this.name = name;
        this.department = department;
    }
}