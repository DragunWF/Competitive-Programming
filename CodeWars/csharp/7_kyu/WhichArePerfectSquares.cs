// https://www.codewars.com/kata/53227465e4d01b5d5200011e/train/csharp

using System.Collections.Generic;
using static System.Math;

public class Kata {
  public static int[] GetSquares(int[] array) {
    List < int > perfectSquares = new();
    for (int i = 0; i < array.Length; i++) {
      if (!perfectSquares.Contains(array[i]) && IsPerfectSquare(array[i])) {
        perfectSquares.Add(array[i]);
      }
    }
    perfectSquares.Sort();
    return perfectSquares.ToArray();
  }

  private static bool IsPerfectSquare(int num) {
    if (num < 0) return false;
    if (num == 0 || num == 1) return true;
    int root = (int) Sqrt(num);
    return root * root == num;
  }
}