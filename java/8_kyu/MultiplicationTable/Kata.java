// https://www.codewars.com/kata/5a2fd38b55519ed98f0000ce/train/java

class Kata {
    public static String multiTable(int num) {
        StringBuilder output = new StringBuilder();
        for (int i = 1; i <= 10; i++)
            output.append(String.format("%s * %s = %s\n", i, num, i * num));
        return output.toString();
    }
}
