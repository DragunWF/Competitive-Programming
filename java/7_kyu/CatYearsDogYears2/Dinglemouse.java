// https://www.codewars.com/kata/5a6d3bd238f80014a2000187/train/java

import java.util.Arrays;

public class Dinglemouse {
    public static int[] ownedCatAndDog(final int catYears, final int dogYears) {
        return new int[] { calculateAnimalYears(catYears, true), calculateAnimalYears(dogYears, false) };
    }

    private static int calculateAnimalYears(int animalYears, boolean isCat) {
        if (animalYears < 15)
            return 0;
        animalYears -= 15;
        if (animalYears >= 9) {
            animalYears -= 9;
            if (animalYears <= 0)
                return 2;
        } else
            return 1;
        return animalYears / (isCat ? 4 : 5) + 2;
    }

    public static void main(String[] args) {
        // Not part of the solution, just testing
        System.out.println(Arrays.toString(ownedCatAndDog(15, 15))); // 1, 1
        System.out.println(Arrays.toString(ownedCatAndDog(56, 64))); // 10, 10
    }
}