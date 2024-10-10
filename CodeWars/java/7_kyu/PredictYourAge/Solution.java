// https://www.codewars.com/kata/5aff237c578a14752d0035ae/train/java

public class Solution {
    public static int predictAge(int age1, int age2, int age3, int age4, int age5, int age6, int age7, int age8) {
        double[] ages = { age1, age2, age3, age4, age5, age6, age7, age8 };
        double sum = 0;
        for (double age : ages) {
            sum += age * age;
        }
        return (int) Math.sqrt(sum) / 2;
    }
}