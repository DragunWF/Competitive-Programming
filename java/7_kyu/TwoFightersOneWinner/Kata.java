// https://www.codewars.com/kata/577bd8d4ae2807c64b00045b/train/java

public class Kata {
  public static String declareWinner(Fighter fighter1, Fighter fighter2, String firstAttacker) {
    return fighter1.name.equals(firstAttacker) ? combatLoop(fighter1, fighter2) : combatLoop(fighter2, fighter1);
  }

  public static String combatLoop(Fighter first, Fighter second) {
    boolean isFirstTurn = true;
    while (first.health > 0 && second.health > 0) {
      if (isFirstTurn)
        second.health -= first.damagePerAttack;
      else
        first.health -= second.damagePerAttack;
      isFirstTurn = !isFirstTurn;
    }
    return first.health > 0 ? first.name : second.name;
  }

  public static void main(String[] args) {
    // Not part of the solution, just testing
    System.out.println(Kata.declareWinner(new Fighter("Lew", 10, 2), new Fighter("Harry", 5, 4), "Lew"));
  }
}

class Fighter {
  public String name;
  public int health, damagePerAttack;

  public Fighter(String name, int health, int damagePerAttack) {
    this.name = name;
    this.health = health;
    this.damagePerAttack = damagePerAttack;
  }
}

// XOR