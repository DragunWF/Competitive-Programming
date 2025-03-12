// https://www.codewars.com/kata/57f7b8271e3d9283300000b4/train/java

public class Kata {
    public static String evenOrOdd(String str) {
        int evenSum = 0;
        int oddSum = 0;
        for (int i = 0; i < str.length(); i++) {
            int num = Integer.parseInt(String.valueOf(str.charAt(i)));
            if (num % 2 == 0) {
                evenSum += num;
            } else {
                oddSum += num;
            }
        }

        if (evenSum == oddSum) {
            return "Even and Odd are the same";
        }
        return evenSum > oddSum ? "Even is greater than Odd" : "Odd is greater than Even";
    }
}