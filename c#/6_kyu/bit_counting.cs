using System;

public class Kata
{
  public static int CountBits(int n)
  {
    var binary = Convert.ToString(n, 2);
    var count = 0;
    foreach (byte num in binary)
      if (num == '1') count++;
    return count;
  }
}

// https://www.codewars.com/kata/526571aae218b8ee490006f4/train/csharp