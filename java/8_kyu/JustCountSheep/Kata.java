// https://www.codewars.com/kata/5b077ebdaf15be5c7f000077/train/java

class Kata {
    public static String countingSheep(int num) {
        String output = "";
        for (int i = 1; i <= num; i++)
            output += String.format("%s sheep...", i);
        return output;
    }
}