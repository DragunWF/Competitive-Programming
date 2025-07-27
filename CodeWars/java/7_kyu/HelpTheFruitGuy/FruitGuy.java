// https://www.codewars.com/kata/557af4c6169ac832300000ba/train/java

public class FruitGuy {
    public static String[] removeRotten(String[] fruitBasket) {
        if (fruitBasket == null) {
            return new String[0];
        }
        
        String[] output = new String[fruitBasket.length];
        for (int i = 0; i < fruitBasket.length; i++) {
            if (fruitBasket[i].contains("rotten")) {
                output[i] = fruitBasket[i].replace("rotten", "").toLowerCase();
                continue;
            }
            output[i] = fruitBasket[i];
        }
        return output;
    }
}