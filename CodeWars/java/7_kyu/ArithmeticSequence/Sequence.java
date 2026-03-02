// https://www.codewars.com/kata/540f8a19a7d43d24ac001018/train/java

public class Sequence {
  public static int nthterm(int first, int n, int c) {
    int nthTerm = 0;
    int currentNum = first;
    while (nthTerm < n) {
        currentNum += c;
        nthTerm++;
    }
    return currentNum;
  }
}