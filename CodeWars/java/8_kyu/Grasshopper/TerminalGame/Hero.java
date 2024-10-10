// https://www.codewars.com/kata/55e8aba23d399a59500000ce/train/java

public class Hero {
    public String name;
    public String position = "00";
    public int experience = 0;
    public int health = 100;
    public int damage = 5;

    public Hero() {
        name = "Hero";
    }

    public Hero(String name) {
        this.name = name;
    }
}