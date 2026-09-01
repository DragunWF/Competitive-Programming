// https://www.codewars.com/kata/576400f2f716ca816d001614/train/java

public class Reduce{
  public static int[] myFraction(int[] fractions){
    int gcd = getGcd(fractions[0], fractions[1]);
    return new int[]{ fractions[0] / gcd, fractions[1] / gcd };
  }

  public static int getGcd(int firstNum, int secondNum) {
    while (secondNum != 0) {
      int temp = secondNum;
      secondNum = firstNum % secondNum;
      firstNum = temp;
    }
    return Math.abs(firstNum);
  }
}