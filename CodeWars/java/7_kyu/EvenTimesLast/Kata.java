// https://www.codewars.com/kata/5a1a9e5032b8b98477000004/train/java

public class Kata {
    public static int evenLast(int[] numbers) {
       if (numbers.length == 0) {
         return 0;
       }
      
       int evenSum = 0;
       for (int i = 0; i < numbers.length; i++) {
          if (i % 2 == 0) {
              evenSum += numbers[i];
          }
       }
       return evenSum * numbers[numbers.length - 1];
    }
}